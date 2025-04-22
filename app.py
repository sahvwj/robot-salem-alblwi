from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def home():
    return app.send_static_file('واجهة روبوت سالم النسخه المحسنه.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '').lower()

    if any(word in user_message for word in ["هلا", "أهلين", "مرحبا", "السلام", "صباح", "مساء"]):
        response = random.choice(["هلا والله!", "نورت!", "حيّاك الله!", "أسعد الله وقتك!"])
    elif any(word in user_message for word in ["كيفك", "اخبارك", "طمني", "وش علومك", "كيف الحال"]):
        response = random.choice(["تمام وانت؟", "الحمد لله بخير، وأنت؟", "أنا بخير دامك بخير"])
    elif any(word in user_message for word in ["احبك", "أشتقت", "أعزك", "غالي", "فديتك", "اموت فيك"]):
        response = "حتى أنا أحبك يا أبوي! قلبي كبير لك."
    elif any(word in user_message for word in ["نواف"]):
        response = "نواف هو نواف عوده سالم ابن مشغب العرادي، ابن عم المطور سالم الذي قام بتطويري."
    elif any(word in user_message for word in ["الوجه"]):
        response = "الوجه هي مدينة ساحلية جميلة."
    elif any(word in user_message for word in ["ابو العجاج", "أبو العجاج"]):
        response = (
            "أبو العجاج هي قرية زراعية جميلة ورائعة جدًا. من أهم مواقعها:
"
            "١- الفرش
٢- الدحو
٣- أبو دومه
٤- الخضراء
٥- أبو سيالة"
        )
    elif any(word in user_message for word in ["باي", "مع السلامه", "اشوفك", "بطلع"]):
        response = "مع السلامة! نشوفك على خير يا غالي."
    else:
        response = "ما فهمت عليك، جرب تقولها بطريقة ثانية؟ أو اشرح لي أكثر."

    return jsonify({"reply": response})

if __name__ == '__main__':
    app.run(debug=True)