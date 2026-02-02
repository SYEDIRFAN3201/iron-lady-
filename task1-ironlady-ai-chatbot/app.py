from flask import Flask, render_template, request, jsonify

# ----------------------------
# APP SETUP
# ----------------------------
app = Flask(__name__)

# ----------------------------
# HOME PAGE
# ----------------------------
@app.route("/")
def home():
    return render_template("index.html")

# ----------------------------
# CHAT API (FALLBACK AI LOGIC)
# ----------------------------
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").lower()

    if "working woman" in user_message or "help me" in user_message:
        reply = (
            "Iron Lady supports working women through leadership development programs, "
            "career guidance, skill-building workshops, and mentorship. "
            "We help women grow professionally, gain confidence, and achieve career goals."
        )

    elif "career" in user_message:
        reply = (
            "Iron Lady helps women plan their career growth through mentoring, "
            "leadership training, and structured learning paths."
        )

    elif "program" in user_message or "courses" in user_message:
        reply = (
            "Iron Lady offers leadership programs, career acceleration workshops, "
            "mentorship initiatives, and community learning for women professionals."
        )

    elif "contact" in user_message or "join" in user_message:
        reply = (
            "You can join Iron Lady by visiting our official website or enrolling "
            "in one of our leadership and career development programs."
        )

    else:
        reply = (
            "Iron Lady is an AI-powered career guide designed to support women "
            "professionals through learning, mentorship, and leadership development."
        )

    return jsonify({"reply": reply})

# ----------------------------
# RUN SERVER
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)
