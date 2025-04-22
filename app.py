from flask import Flask, request, render_template_string
import random

app = Flask(__name__)

responses = {
    "ترحيب": ["هلا والله!", "نورت!", "حيّاك الله!", "أسعد الله وقتك!"],
    "الحال": ["تمام وانت؟", "الحمد لله بخير، وأنت؟", "أنا بخير دامك بخير"],
    "حب": ["حتى أنا أحبك يا أبوي! قلبي كبير لك."],
    "حزن": ["وش فيك يا بعد قلبي؟ أنا معك.", "لا تزعل، الدنيا ما تستاهل... تكلم معي وفضفض.", "إذا ضايق صدرك، اعتبرني أخوك واسولف."],
    "فرح": ["فرحت لك والله! دايمًا مبسوط إن شاء الله!", "حماس! خليني أفرح معك!", "الله يديم سعادتك يا الغالي!"],
    "قبيلة بلي": ["قبيلة بلي هم أحفاد الصحابة، من أعظم القبائل العربية وأهل كرم وشجاعة وتاريخ مشرف."],
    "نواف": ["نواف هو نواف عوده سالم ابن مشغب العرادي، ابن عم المطور سالم الذي قام بتطويري."],
    "الوجه": ["الوجه هي مدينة ساحلية جميلة."],
    "أبو العجاج": ["أبو العجاج هي قرية زراعية جميلة ورائعة جدًا، من أهم مواقعها: الفرش، الدحو، أبو دومه، الخضراء، وأبو سيالة."],
    "تعريف": ["أنا روبوت ذكي تم برمجتي على يد سالم العرادي.", "مساعد ذكي أقدر أضحكك، ألعب معك، وأكون دايم معك.", "أنا برنامج بسيط… لكن معك أكون شيء كبير!"],
    "طفش": ["تبي نلعب؟ عندي حجر ورقة مقص!", "أقول لك نكته؟ ولا نسولف؟", "افتح لك شي يونسك... أو خلنا نتكلم شوي!"],
    "نكت": ["فيه جني طاح من الدرج... صار جنّي مكسور!", "ليه الكمبيوتر ما يضحك؟ لأنه مخزن النكت!", "فيه واحد سأل صاحبه: تحب المرتفعات؟ قال: أعشق سطح الثلاجة!"],
    "شكر": ["العفو يا بطل!", "ولا يهمك!", "أي وقت!"],
    "وداع": ["مع السلامة! نشوفك على خير يا غالي."]
}

@app.route('/', methods=['GET', 'POST'])
def index():
    reply = ""
    if request.method == 'POST':
        msg = request.form['message'].lower()
        if any(w in msg for w in ["هلا", "أهلين", "السلام", "مرحبا", "صباح", "مساء"]):
            reply = random.choice(responses["ترحيب"])
        elif any(w in msg for w in ["كيفك", "اخبارك", "طمني", "وش علومك", "كيف الحال"]):
            reply = random.choice(responses["الحال"])
        elif any(w in msg for w in ["احبك", "أشتقت", "أعزك", "غالي", "فديتك", "اموت فيك"]):
            reply = responses["حب"][0]
        elif any(w in msg for w in ["زعلان", "مضايق", "تعبان", "حزين"]):
            reply = random.choice(responses["حزن"])
        elif any(w in msg for w in ["فرحان", "مبسوط", "سعيد", "متحمس"]):
            reply = random.choice(responses["فرح"])
        elif "بلي" in msg:
            reply = responses["قبيلة بلي"][0]
        elif "نواف" in msg:
            reply = responses["نواف"][0]
        elif "الوجه" in msg:
            reply = responses["الوجه"][0]
        elif "ابو العجاج" in msg or "أبو العجاج" in msg:
            reply = responses["أبو العجاج"][0]
        elif any(w in msg for w in ["من انت", "وش انت", "وش اسمك", "تعرفني على نفسك"]):
            reply = random.choice(responses["تعريف"])
        elif any(w in msg for w in ["طفشان", "ملل", "زهقان", "طفش"]):
            reply = random.choice(responses["طفش"])
        elif "نكت" in msg:
            reply = random.choice(responses["نكت"])
        elif any(w in msg for w in ["شكرا", "ثانكس", "مشكور"]):
            reply = random.choice(responses["شكر"])
        elif any(w in msg for w in ["باي", "مع السلامه", "اشوفك", "بطلع"]):
            reply = responses["وداع"][0]
        else:
            reply = "ما فهمت عليك، جرب تقولها بطريقة ثانية؟ أو اشرح لي أكثر."

    return render_template_string("""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>روبوت سالم البلوي</title>
</head>
<body style="font-family: Arial; text-align: center;">
    <h2>أهلاً بك في روبوت سالم البلوي!</h2>
    <form method="POST">
        <input name="message" style="width: 300px;" placeholder="اكتب رسالتك هنا">
        <button type="submit">إرسال</button>
    </form>
    {% if reply %}
        <h3>الرد: {{ reply }}</h3>
    {% endif %}
</body>
</html>""", reply=reply)

if __name__ == "__main__":
    app.run()