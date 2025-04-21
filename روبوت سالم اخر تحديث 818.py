import random

while True:
    message = input("أنت: ").lower()

    if any(word in message for word in ["هلا", "أهلين", "مرحبا", "السلام", "صباح", "مساء"]):
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

    elif "نلعب" in message:
        print("روبوت: يلا نلعب! اكتب: حجر، ورقة، أو مقص")
        user_choice = input("أنت: ").lower()
        options = ["حجر", "ورقة", "مقص"]
        bot_choice = random.choice(options)
        print("روبوت: أنا اخترت:", bot_choice)

        if user_choice == bot_choice:
            reply = "تعادلنا!"
        elif (
            (user_choice == "حجر" and bot_choice == "مقص") or
            (user_choice == "ورقة" and bot_choice == "حجر") or
            (user_choice == "مقص" and bot_choice == "ورقة")
        ):
            reply = "فزت علي! مبروك"
        elif user_choice in options:
            reply = "أنا اللي فزت! حاول مره ثانية"
        else:
            reply = "ما فهمت اختيارك، لازم تختار: حجر، ورقة، أو مقص"

    elif any(word in message for word in ["باي", "مع السلامه", "اشوفك", "بطلع"]):
        reply = "مع السلامة! نشوفك على خير يا غالي."
        print("روبوت:", reply)
        break

    elif "نواف" in message:
        reply = "نواف هو نواف عوده سالم ابن مشغب العرادي، ابن عم المطور سالم الذي قام بتطويري."

    elif "الوجه" in message:
        reply = "الوجه هي مدينة ساحلية جميلة."

    elif "ابو العجاج" in message:
        reply = (
            "ابو العجاج هي قرية زراعية جميلة ورائعة جداً. من أهم المواقع فيها:
"
            "١- الفرش
٢- الدحو
٣- ابو دومه
٤- الخضراء
٥- ابو سيالة"
        )

    else:
        reply = "ما فهمت عليك، جرب تقولها بطريقة ثانية؟ أو اشرح لي أكثر."

    print("روبوت:", reply)

    with open("log.txt", "a", encoding="utf-8") as log:
        log.write("أنت: " + message + "\n")
        log.write("روبوت: " + reply + "\n")
