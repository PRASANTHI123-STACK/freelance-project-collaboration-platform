from flask import Flask, request
from flask_socketio import SocketIO, join_room, leave_room, emit

app = Flask(__name__)

# ============================================================
# SOCKET.IO CONFIGURATION
# ============================================================

socketio = SocketIO(
    app,
    cors_allowed_origins="*"
)


# ============================================================
# ROOM STORAGE
# ============================================================

# Example:
# rooms = {
#     "project-101": ["socket-id-1", "socket-id-2"]
# }

rooms = {}

# Store which room each socket is currently in
user_rooms = {}


# ============================================================
# HOME
# ============================================================

@app.route("/")
def home():

    return """
    <!DOCTYPE html>

    <html>

    <head>

        <title>FreelanceHub Backend</title>

    </head>

    <body>

        <h1>FreelanceHub Backend</h1>

        <p>
            Backend server is running successfully.
        </p>

    </body>

    </html>
    """


# ============================================================
# JOIN ROOM
# ============================================================

@socketio.on("join-room")
def handle_join_room(data):

    room = data.get("room")

    if not room:

        emit(
            "room-error",
            {
                "message": "Room ID is required."
            }
        )

        return


    sid = request.sid


    # --------------------------------------------------------
    # Prevent duplicate joining
    # --------------------------------------------------------

    if sid in user_rooms:

        existing_room = user_rooms[sid]

        if existing_room == room:

            return

        leave_room(existing_room)

        if existing_room in rooms:

            if sid in rooms[existing_room]:

                rooms[existing_room].remove(sid)

            if len(rooms[existing_room]) == 0:

                del rooms[existing_room]


        del user_rooms[sid]


    # --------------------------------------------------------
    # Create room if necessary
    # --------------------------------------------------------

    if room not in rooms:

        rooms[room] = []


    # --------------------------------------------------------
    # Maximum 2 participants
    # --------------------------------------------------------

    if len(rooms[room]) >= 2:

        emit(
            "room-full",
            {
                "message": "This video call already has two participants."
            }
        )

        print(
            f"Room full: {room}"
        )

        return


    # --------------------------------------------------------
    # Join Socket.IO room
    # --------------------------------------------------------

    join_room(room)


    rooms[room].append(sid)

    user_rooms[sid] = room


    current_users = len(rooms[room])


    # --------------------------------------------------------
    # Determine role
    # --------------------------------------------------------

    if current_users == 1:

        role = "caller"

    else:

        role = "receiver"


    # --------------------------------------------------------
    # Tell current user that they joined
    # --------------------------------------------------------

    emit(
        "room-joined",
        {
            "role": role,
            "users": current_users,
            "room": room,
            "sid": sid
        }
    )


    # --------------------------------------------------------
    # If second participant joins
    # --------------------------------------------------------

    if current_users == 2:

        existing_user = rooms[room][0]

        new_user = rooms[room][1]


        # Tell first participant about second participant

        emit(
            "user-joined",
            {
                "sid": new_user
            },
            to=existing_user
        )


        # Tell second participant about first participant

        emit(
            "user-joined",
            {
                "sid": existing_user
            },
            to=new_user
        )


        # Notify room that participant is ready

        emit(
            "participant-joined",
            {
                "users": 2
            },
            room=room
        )


    print(
        f"User joined room: {room} | "
        f"Users: {current_users} | "
        f"Role: {role} | "
        f"SID: {sid}"
    )


# ============================================================
# CALL STARTED
# ============================================================

@socketio.on("call-started")
def handle_call_started(data):

    room = data.get("room")

    if not room:

        return


    emit(
        "call-started",
        {
            "sender": request.sid
        },
        room=room,
        include_self=False
    )


    print(
        f"Call started in room: {room}"
    )


# ============================================================
# OFFER
# ============================================================

@socketio.on("offer")
def handle_offer(data):

    room = data.get("room")

    offer = data.get("offer")

    target = data.get("target")


    if not room or not offer:

        return


    sender = request.sid


    message = {
        "offer": offer,
        "sender": sender
    }


    # Send directly to target

    if target:

        emit(
            "offer",
            message,
            to=target
        )


    # Otherwise broadcast to room

    else:

        emit(
            "offer",
            message,
            room=room,
            include_self=False
        )


    print(
        f"Offer sent | "
        f"Room: {room} | "
        f"From: {sender} | "
        f"To: {target}"
    )


# ============================================================
# ANSWER
# ============================================================

@socketio.on("answer")
def handle_answer(data):

    room = data.get("room")

    answer = data.get("answer")

    target = data.get("target")


    if not room or not answer:

        return


    sender = request.sid


    message = {
        "answer": answer,
        "sender": sender
    }


    # Send directly to target

    if target:

        emit(
            "answer",
            message,
            to=target
        )


    # Otherwise broadcast to room

    else:

        emit(
            "answer",
            message,
            room=room,
            include_self=False
        )


    print(
        f"Answer sent | "
        f"Room: {room} | "
        f"From: {sender} | "
        f"To: {target}"
    )


# ============================================================
# ICE CANDIDATE
# ============================================================

@socketio.on("ice-candidate")
def handle_ice_candidate(data):

    room = data.get("room")

    candidate = data.get("candidate")

    target = data.get("target")


    if not room or not candidate:

        return


    sender = request.sid


    message = {
        "candidate": candidate,
        "sender": sender
    }


    # Send directly to target

    if target:

        emit(
            "ice-candidate",
            message,
            to=target
        )


    # Otherwise broadcast to room

    else:

        emit(
            "ice-candidate",
            message,
            room=room,
            include_self=False
        )


# ============================================================
# END CALL
# ============================================================

@socketio.on("end-call")
def handle_end_call(data):

    room = data.get("room")

    if not room:

        return


    emit(
        "call-ended",
        {
            "sender": request.sid
        },
        room=room,
        include_self=False
    )


    print(
        f"Call ended in room: {room}"
    )


# ============================================================
# DISCONNECT
# ============================================================

@socketio.on("disconnect")
def handle_disconnect():

    sid = request.sid

    room = user_rooms.get(sid)


    if not room:

        print(
            f"User disconnected: {sid}"
        )

        return


    # --------------------------------------------------------
    # Remove from room
    # --------------------------------------------------------

    if room in rooms:

        if sid in rooms[room]:

            rooms[room].remove(sid)


        # Tell remaining participant

        emit(
            "user-left",
            {
                "sid": sid
            },
            room=room,
            include_self=False
        )


        # Delete empty room

        if len(rooms[room]) == 0:

            del rooms[room]


    # --------------------------------------------------------
    # Remove socket mapping
    # --------------------------------------------------------

    if sid in user_rooms:

        del user_rooms[sid]


    print(
        f"User disconnected | "
        f"Room: {room} | "
        f"SID: {sid}"
    )


# ============================================================
# START SERVER
# ============================================================

if __name__ == "__main__":

    print("======================================")

    print(
        "FreelanceHub Video Call Backend"
    )

    print("======================================")

    print(
        "Server running on:"
    )

    print(
        "http://0.0.0.0:8000"
    )

    print("======================================")


    socketio.run(
        app,
        host="0.0.0.0",
        port=8000,
        debug=True,
        allow_unsafe_werkzeug=True
    )