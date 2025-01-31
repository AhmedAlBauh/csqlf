import telebot
from telebot import types
import logging

# تفعيل التسجيل للأخطاء
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# قائمة القوانين المرقمة
LAWS = [
    "1. القانون: يخطأ القلب لحظه فيعاقبه العقل سنين😓",
    "2. القانون: لا تنظر للوراء فهناك ماضي يؤلمك ولا تنظر الى الامام فهناك مستقبل يقلقك بل انظر الى الاعلى فهناك رب يسعدك",
    "3. القانون: لن تتوقف الحياة على اشياء خذلتنا فدائما يعوضنا الله بما هو افضل",
    "4. القانون: كن كالرقم 1 في جدول الضرب لا يعطي احدا اكثر من قيمته",
    "5. القانون: الحب كلمه صغيره سمعتها عجبتني جربتها قتلتني",
    "6. القانون: الصلاه مثل الشمس و انت القمر فلن يضيئ القمر بدون شمس و لن يكون القمر جميلاً لو لم يكن حولة ذالك الظلام",
    "7. القانون: لااحد يناديك من أجل مصلحتك الا المؤذن",
    "8. القانون: كن من تكون فاليوم تمشي وغدا مدفون",
    "9. القانون: اتمنى لك السعاده أكبر كذبة تقال عند الوداع",
    "10. القانون: الحياة دروس وتجارب والرضا بالله والتقدير للنفس هما المفتاح لتجاوز الخذلان والتحديات❤️",
    "11. القانون: لا تستمع لمن يعاديك فالله الذي يحميك",
    "12. القانون: لا تكن على أخطائك محامي وعلى خطأ الناس قاضي",
    "13. القانون: لا تحزن لمن يطعنك فالله دومن معك",
    "14. القانون: الاعتذار شجاعه والتسامح قوة",
    "15. القانون: في كل علاقه بدايه لا ترضي الله ونهاية لا ترضيك",
    "16. القانون: لا تحسب ان الذين قتلوا رحلوا بل عند الله اجل عظيم",
    "17. القانون: لا قانون ضد القوانين وهذه هي الحياة",
    "18. القانون: لن تكسرك الحياة اذا اتقنت فن الصبر",
    "19. القانون: راحة القلب في قلة الاهتمام",
    "20. القانون: الجاهل يعرف بكلامه والحكيم يعرف بصمته",
    "21. القانون: لا تحرق نفسك من اجل الناس فالشمس احرقت نفسها من اجل الاخرين ومازلنا نحب القمر",
    "22. القانون: إن فقد البصر اهم من فقد بصيره",
    "23. القانون: الفراشه رغم جمالها حشره والصبار رغم قسوته زهره فلا تحكم على الناس من اسمائهم و اشكالهم",
    "24. القانون: إن الحياه الغير مدروسه لا تستحق العيش",
    "25. القانون: عندما لا يفهمك احد فجرب السجود وحادث ربك الموجود",
    "26. القانون: يعاتبوك علئ تصرفاتك اما عن تصرفاتهم لا عين بصر ولا اذن تسمع ولا ضمير يشعر",
    "27. القانون: لا تتوقف الحياة بسبب بعض خيبات الامل فالوقت لا يتوقف عندما تتعطل الساعه",
    "28. القانون: عندما يحطم الجميع احلامك اعرف ان انت على وشك الوصول اليها",
    "29. القانون: عدد سكان العالم 7870851405 تجاهل كلامهم مثلما تجاهلت قراءة الرقم",
    "30. القانون: الدنيه قوسان الاول بدايتك والثاني نهايتك فضع بينهما شيئا نافعا يتذكرك به الناس",
    "31. القانون: أن الله الذي اختار لك طريقك من أوله لن يتركك في منتصفه فأطمأن",
    "32. القانون: تتأخر وكأنها ليست من نصيبك ثم يبهرك الله بطريقة تحقيقها",
    "33. القانون: ثق بما سياتي من الله قلها ونفسك راضيه",
    "34. القانون: مهما كنت حزيناً ومهما ضاقت عليك الدنيا ومهما عصيت تذكر أن رحمه الله واسعه",
    "35. القانون: كن كالحياة رافق الجميع ولا تتمسك بأحد",
    "36. القانون: كالعادة يا سادة الصلاه على النبي هي مصدر السعاده",
    "37. القانون: لا توجد حياة بلا تحديات فهي التي تصقل قوتك وإصرارك تقبَّل الصعوبات كفرص للتطور واستمر بالمحاولة مهما كان الطريق صعبًا✨",
    "38. القانون: اشتاق لك واجبّر الشوق بالصمت وعمر صمتي ماكان معناه نسيانك",
    "39. القانون: لا تكن سجينا لماضيك لقد كان درسا فقط وليس حكما مؤبد",
    "40. القانون: لَا تَدَعْ اَلْخَوْفَ يَمْنَعُكَ مِنَ اَلْمُحَاوَلَةِ فَاَلْخَسَارَةُ اَلْكُبْرَى هِيَ اَلاِسْتِسْلَامُ قَبْلَ اَلْبِدَايَةِ",
    "41. القانون: الحياه رواية جميلة عليك قرائتها حتى النهايه لا تتوقف ابدا عند سطر حزين فقد تكون النهايه جميلة",
    "42. القانون: لا ترتَجي النُور بَل كُن أنتَ مصدَرُه و كُن لِنفسِك قومًا إن هُم هجَروا",
    "43. القانون: الحياة كالبحر من لم يحسن العوم فيها فقذفت به الامواج",
    "44. القانون: لا شيء يُعذب الإنسان مِثل كِتمان حُزنه",
    "45. القانون: أمشي على قدمك المكسورة ولا تترك أثر يدك على كتف أحد",
    "46. القانون: يومًا ما ستدرك أن أقسى ما مررت به كان خيرًا عظيمًا أنقذك ليجعلك أقوى مما كنت عليه",
    "47. القانون: قم فلا وقت للخيبة هناك جميل ينتظرك فاسعى إليه قم واكسر كل شعور سيء داخلك لم تخلق نفسك لتعذبها خلقت لتكون داعمًا لها في صنع المستحيل فكن ذا أثر",
    "48. القانون: مهما كُنت شخصاً صالحاً سيحكم عليك أشخاص بحسب مزاجهم وحاجتهم",
    "49. القانون: الظروف ماتبعد لاصاحب ولا حبيب الوافي لو يحب من قلبه مايبتعد❤️✌️",
    "50. القانون: من احتاجني لقاني كُنت مجرد محطة انتظار ليرتاح عندها أُناس ثم يرحلون",
    "51. القانون: الأمل صديق رائع ربّما يغيب ولكن لا يخون",
    "52. القانون: وتأخذني بدايات الصباح نحوك وكأنها تود أن تجعل منك فكرة يومي الأولى♥️",
    "53. القانون: لكي لا تخسر نفسك لا تقلد غيرك لا تقارن حياتك بالآخرين لا تتحدى إلا ذاتك ولا تنتقد امراً وانت لم تجربه",
    "54. القانون: أن تضيء شمعة صغيرة خير لك من أن تنفق عمرك تلعن الظلام",
    "55. القانون: كل ما زاد الغرور قل السرور",
    "56. القانون: اعلم ان النزول الوحيد الذي يرفعك هو السجود لله",
    "57. القانون: الملح في الماء يذوب والصلاه على النبي تمحي الذنوب صلي على النبي يا صديقي",
    "58. القانون: يسقط المطر حين يعجز السحاب عن حمل ثقل الماء وتسقط الدموع حين يعجز القلب على تحمل الالم",
    "59. القانون: دع الحرص على الدنيا و في العيش فلا تطمع و لا تجمع من المال فلا تدري لمن تجمع فان الرزق مقسوم و سوء الضن لا ينفع",
    "60. القانون: لا تظن الهدوء الذي تراه في الوجوه يدل على الرضا لكل إنسان شيء في داخله يهزه ويتعبه",
    "61. القانون: كُل الأصَدقاء أصَدقاء لكِن بيَنهم واحِد يَكُون جَميِع الأصَدقِاء🤍",
    "62. القانون: ليس كل من إعتذر مخطئ أو ضعيف الإعتذار صفة نادره لا تجدها إلا في الأوفياء",
    "63. القانون: الاستغباء وأنت فاهم متعه عظيمه",
    "64. القانون: لو كان لك نصيب في شيء ما حتى ولو كانت كل الطرق اليه مستحيلة الله بلطفه سيرتب لك كل الأسباب حتى يصبح بين يديك",
    "65. القانون: ﺗﻔﺎَءل ﺩﺍﺋﻤﺎً ﻻﻥ ﺍﻟﺤﻴﺎﺓ ﺃﺟﻤﻞ ﺑﻜﺜﻴﺮ ﻣﻦ ﺑﺸﺎﻋﺔ ﺍﻟﺤﺰﻥ ﺍﺑﺘﺴﻢ ﺳﺎﻣﺢ ﺍﺳﺘﻤﺘﻊ ﻭﻛﻦ ﻋﻠﻰ ﻳﻘﻴﻦ ﻟﻦ ﻳﺼﻴﺒﻨﺎ ﺇﻻ ﻣﺎ ﻛﺘﺒﻪ ﺍﻟﻠﻪ لنا",
    "66. القانون: لاتخف من التقدم البطيء مادمت لا تقف وتسير نحو الامام",
    "67. القانون: إذا كنت لا تستطيع الطيران فاركض وإذا لم تستطع الركض فامشِ وإذا لم تستطع المشي فازحف لكن مهما فعلت استمر في التقدم للأمام",
    "68. القانون: الحياة ليست بحثًا عن الذات بل هي بناء الذات كل يوم هو فرصة جديدة لتشكيل شخصيتك وصنع مستقبلك فلا تنتظر أن تجد نفسك بل اسعَ لتكون ما تريد أن تكونه",
    "69. القانون: ما كل ما يتمنى المرء يدركه تجري الرياح بما لا تشتهي السفن",
    "70. القانون: الحياة ليست انتظار العاصفة لتصفو بل تعلم الرقص تحت المطر",
    "71. القانون: لاتَكن ليناً فَتُعصرْ ولا تَكن صلباً فتكسر فخير الامور اوسطها",
    "72. القانون: إذا لم تستطع تغيير الظروف غيّر طريقة نظرتك لها فالقوة تبدأ من داخلك",
    "73. القانون: لم تكن القناة قادره على انشار القوانين لدى القناة ظروف وهي امتحانات نصف السنه فنرجو منكم المعذره♥🌹🥺",
    "74. القانون: الطريق ليس طويل بل هو مسار ينتظر الخطوة الاولى وليس بعيدا بل هي الاوهام فلا تنظر لسراط غيرك واتعظ من خطاك",
    "75. القانون: لاتأيس ولاتفقد الامل فهناك طريق ينير حياتك فقط اصبر والله سييسر لك الخير",
    "76. القانون: غباء منك ان تكون حزين بسبب شخص يعيش حياته بكل سعاده",
    "77. القانون: لاتدعي خيرا وانت نائما ليس لك حمل تجتهد ولاتدعي شرا على شخص يدعوك خيرا فيوم القيامة خصيمك او رحيمك",
    "78. القانون: لا تحزن على من ينسى فهو يعيش وأنت الأسى اخرج وابدأ عهدًا جديدًا فالحياة تمضي لمن قسا",
    "79. القانون: غباء منك ان تخاف من شخص خلقه الله مثلك",
    "80. القانون: لاتخف لاتقلق لاتتردد لاتنسى لاتخف فما دمت تعرف الله فالله يبعد عنك الشر لاتقلق من شيء فاذا كان سوء فاراد الله به الخير لاتترد فالله معك لاتنسى ذكر الله الذي دوما معك واكرمك بنعمه",
    "81. القانون: إذا ضاقت بك الحياة وأظلمت دروبها فتذكّر أن الله أقرب إليك من حبل الوريد يسمع شكواك ويرى دموعك ولن يتركك وحيدًا أبدًا",
    "82. القانون: احذر عدوك مرة وصديقك ألف مرة فإن انقلب الصديق فهو أعلم بالمضرة",
    "83. القانون: تحسن الظن فتندم خير من ان تسيئه فتظلم",
    "84. القانون: لا تحسب ان الصمت ضعف فلقناص يحبس أنفاسه لكي ينهي عن انفاسك",
    "85. القانون: لا تراقب الساعة افعل كما تفعل استمر بالمضي قدمًا",
    "86. القانون: لا تقلل من قدر نفسك فالجبال كانت في الأصل مجرد صخور صغيرة",
    "87. القانون: النجاح ليس نهاية الطريق والفشل ليس قاتلًا الأهم هو الشجاعة للاستمرار",
    "88. القانون: الصَّلاةُ نُورٌ وَالصَّبرُ مِفتاحُ الفَرَج وَالتَّوَكُّلُ عَلَى اللهِ سَكَنٌ لِلقَلبِ إيَّاكَ أن تَنسَى أنَّ رِزقَكَ مَكتوبٌ وَعُمرَكَ مَعدودٌ فَلا تَطلُبْ إلَّا رِضاهُ وَاذكُرْ قَولَ اللهِ {فَإِنَّ مَعَ العُسرِ يُسرًا إِنَّ مَعَ العُسرِ يُسرًا} فَكُنْ كَالسَّماءِ تَحتَمِلُ الغُيومَ ثِقْ بِأنَّ وَراءَ كُلِّ ألمٍ حِكْمَةٌ وَرَحمةٌ الحَياةُ عِبَادَةٌ فَاجعَلها قُربَانًا",
    "89. القانون: إذا قدرتَ على عدوِّك فاجعل العفوَ عنه شكرًا للقدرة عليه",
    "90. القانون: وَأَقِيمُوا۟ ٱلصَّلَوٰةَ وَءَاتُوا۟ ٱلزَّكَوٰةَ وَٱرْكَعُوا۟ مَعَ ٱلرَّٰكِعِينَ",
    "91. القانون: إِنَّ ٱللَّهَ يَأْمُرُ بِٱلْعَدْلِ وَٱلْإِحْسَٰنِ وَإِيتَآءِ ذِى ٱلْقُرْبَىٰ وَيَنْهَىٰ عَنِ ٱلْفَحْشَآءِ وَٱلْمُنكَرِ وَٱلْبَغْىِ ۚ يَعِظُكُمْ لَعَلَّكُمْ تَذَكَّرُونَ",
    "92. القانون: لا تندم على الماضي تعلم منه فقط💔",
    "93. القانون: الحياةُ كالنهر لا تُقاسُ عُمقُها بطولِها بل بمدى صفاءِ مائِها وقدرتِها على نحتِ الصخرِ بلُطف كنْ كالماء تَتَدفَّقُ بِلا تَكَلُّف تَمْحُو الجبالَ بِلا صَخَب وَتَحمِلُ في جَرْسِكَ أسرارَ الأرضِ والسماء🌊"
]
    # ... (أضف بقية القوانين هنا حتى القانون 93)


# استبدل 'YOUR_TOKEN' ب token البوت الخاص بك
bot = telebot.TeleBot("")

# تعريف الأمر /start
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("بحث عن قوانين 🧠", callback_data='search_laws'))
    keyboard.add(types.InlineKeyboardButton("اقتراح قانون", callback_data='suggest_law'))
    
    bot.send_message(
        message.chat.id,
        "مرحبًا بك في بوت 'دستور الحكم' ⚖️📜\n\n"
        "هنا ستجد أقوال وحكم ملهمة من الفلاسفة والعظماء، بالإضافة إلى دساتير وقوانين مهمة تساعدك على فهم مبادئ العدالة والحكم الرشيد.\n\n"
        "🔹 اطلب حكمة عشوائية بكتابة 'حكمة اليوم'\n"
        "🔹 احصل على اقتباسات قانونية بكتابة 'مادة قانونية'\n"
        "🔹 اكتشف مبادئ الحكم بكتابة 'دستور'\n\n"
        "📌 استمتع بالمعرفة، فالعلم أساس العدل!",
        reply_markup=keyboard
    )

# تعريف زر "بحث عن قوانين"
@bot.callback_query_handler(func=lambda call: call.data == 'search_laws')
def search_laws(call):
    bot.answer_callback_query(call.id)
    bot.send_message(
        call.message.chat.id,
        "أدخل رقم القانون الذي تبحث عنه (مثال: 1، 2، 3، ... حتى 93)."
    )
    bot.register_next_step_handler(call.message, process_law_number)

# معالجة رقم القانون المدخل
def process_law_number(message):
    try:
        law_number = int(message.text)
        if 1 <= law_number <= len(LAWS):
            bot.reply_to(message, LAWS[law_number - 1])
        else:
            bot.reply_to(message, "رقم القانون غير صحيح. الرجاء إدخال رقم بين 1 و 93.")
    except ValueError:
        bot.reply_to(message, "الرجاء إدخال رقم صحيح.")

# تعريف زر "اقتراح قانون"
@bot.callback_query_handler(func=lambda call: call.data == 'suggest_law')
def suggest_law(call):
    bot.answer_callback_query(call.id)
    bot.send_message(
        call.message.chat.id,
        "ارسل القانون إلى هذا البوت وسوف يتم التحقق منه في نفس اليوم @BicenyAibot 🧾"
    )

# معالجة الرسائل النصية
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text

    if text == "حكمة اليوم":
        bot.reply_to(message, "هذه حكمة اليوم: الصبر مفتاح الفرج.")
    elif text == "مادة قانونية":
        bot.reply_to(message, "هذه مادة قانونية: القانون رقم 1 - يخطأ القلب لحظه فيعاقبه العقل سنين.")
    elif text == "دستور":
        bot.reply_to(message, "هذا دستور الحكم: القانون رقم 2 - لا تنظر للوراء فهناك ماضي يؤلمك.")
    else:
        bot.reply_to(message, "لم أفهم طلبك. الرجاء استخدام الأزرار المتاحة.")

# بدأ البوت
if __name__ == '__main__':
    bot.polling(none_stop=True)
