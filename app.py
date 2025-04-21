
from flask import Flask, request, render_template_string
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def chat():
    reply = ""
    user_name = ""
    mode = "عادي"

    if request.method == "POST":
        message = request.form["message"].lower()

        if "اسمي" in message:
            user_name = message.split("اسمي")[-1].strip()
            reply = f"تشرفت فيك يا {user_name}!"

        elif "مزاجك" in message and "رسمي" in message:
            mode = "رسمي"
            reply = "تم تفعيل الوضع الرسمي."

        elif "مزاجك" in message and "فله" in message:
            mode = "فله"
            reply = "أوكي، فله ووناسه شغاله!"

        elif "بيت شعر" in message:
            responses = [
                "أنا الذي نظر الأعمى إلى أدبي ** وأسمعت كلماتي من به صممُ",
                "إذا المرءُ لم يدنسْ من اللؤمِ عرضه ** فكل رداءٍ يرتديه جميلُ",
                "ولم أرَ في عيوب الناس عيباً ** كنقص القادرين على التمامِ"
            ]
            reply = random.choice(responses)

        elif "معلومة" in message:
            responses = [
                "هل تعلم أن قلب الحوت الأزرق بحجم سيارة؟",
                "العسل هو الطعام الوحيد الذي لا يفسد!",
                "عدد عضلات وجه الإنسان حوالي 43 عضلة."
            ]
            reply = random.choice(responses)

        elif any(word in message for word in ["هلا", "أهلين", "مرحبا", "السلام", "صباح", "مساء"]):
            responses = ["هلا والله!", "نورت!", "حيّاك الله!", "أسعد الله وقتك!"]
            reply = random.choice(responses)

        elif any(word in message for word in ["كيفك", "اخبارك", "طمني", "وش علومك", "كيف الحال"]):
            responses = ["تمام وانت؟", "الحمد لله بخير، وأنت؟", "أنا بخير دامك بخير"]
            reply = random.choice(responses)

        elif any(word in message for word in ["احبك", "أشتقت", "أعزك", "غالي", "فديتك", "اموت فيك"]):
            reply = "حتى أنا أحبك يا أبوي! قلبي كبير لك."

        elif any(word in message for word in ["زعلان", "مضايق", "تعبان", "حزين"]):
            responses = [
                "وش فيك يا بعد قلبي؟ أنا معك.",
                "لا تزعل، الدنيا ما تستاهل... تكلم معي وفضفض.",
                "إذا ضايق صدرك، اعتبرني أخوك واسولف."
            ]
            reply = random.choice(responses)

        elif any(word in message for word in ["فرحان", "مبسوط", "سعيد", "متحمس"]):
            responses = [
                "فرحت لك والله! دايمًا مبسوط إن شاء الله!",
                "حماس! خليني أفرح معك!",
                "الله يديم سعادتك يا الغالي!"
            ]
            reply = random.choice(responses)

        elif any(word in message for word in ["بلي", "قبيله بلي", "وش تعرف عن بلي", "وش هي بلي"]):
            reply = "قبيلة بلي هم أحفاد الصحابة، من أعظم القبائل العربية وأهل كرم وشجاعة وتاريخ مشرف."

        elif any(word in message for word in ["من انت", "وش انت", "وش اسمك", "تعرفني على نفسك"]):
            responses = [
                "أنا روبوت ذكي تم برمجتي على يد سالم العرادي.",
                "مساعد ذكي أقدر أضحكك، ألعب معك، وأكون دايم معك.",
                "أنا برنامج بسيط… لكن معك أكون شيء كبير!"
            ]
            reply = random.choice(responses)

        elif any(word in message for word in ["طفشان", "ملل", "زهقان", "طفش"]):
            responses = [
                "تبي نلعب؟ عندي حجر ورقة مقص!",
                "أقول لك نكته؟ ولا نسولف؟",
                "افتح لك شي يونسك... أو خلنا نتكلم شوي!"
            ]
            reply = random.choice(responses)

        elif "نكته" in message or "نكتة" in message:
            responses = [
                "فيه جني طاح من الدرج... صار جنّي مكسور!",
                "ليه الكمبيوتر ما يضحك؟ لأنه مخزن النكت!",
                "فيه واحد سأل صاحبه: تحب المرتفعات؟ قال: أعشق سطح الثلاجة!"
            ]
            reply = random.choice(responses)

        elif any(word in message for word in ["شكرا", "ثانكس", "مشكور"]):
            responses = ["العفو يا بطل!", "ولا يهمك!", "أي وقت!"]
            reply = random.choice(responses)

        elif any(word in message for word in ["نواف"]):
            reply = "نواف هو نواف عوده سالم ابن مشغب العرادي، ابن عم المطور سالم الذي قام بتطويري."

        elif any(word in message for word in ["الوجه"]):
            reply = "الوجه هي مدينة ساحلية جميلة تطل على البحر الأحمر."

        elif any(word in message for word in ["ابو العجاج", "أبو العجاج"]):
            reply = (
                "أبو العجاج هي قرية زراعية جميلة ورائعة جداً. "
                "أهم المواقع فيها واللي يحبها سالم هي: "
                "١- الفرش، ٢- الدحو، ٣- أبو دومه، ٤- الخضراء، ٥- أبو سياله."
            )

        else:
            reply = "ما فهمت عليك، جرب تقولها بطريقة ثانية؟"

    html = """
    <!doctype html>
    <title>روبوت سالم العرادي</title>
    <h1>تحدث مع روبوت سالم</h1>
    <form method=post>
      <input type=text name=message placeholder="اكتب رسالتك هنا">
      <input type=submit value=أرسل>
    </form>
    <p><strong>الروبوت:</strong> {{reply}}</p>
    """
    return render_template_string(html, reply=reply)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
