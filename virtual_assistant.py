import json
import random as Random

class VirtualAssistant:
    childName = ""
    botName = ""
    elderConversations = []
    def __init__(self, childName, elderConversations):
        self.childName = childName
        self.botName = "Virtual Assistant"
        self.elderConversations = elderConversations
    
    def initialSentences(self):
        _initialSentences = [
            f"Merhaba {self.childName}, ben senin arkadaş canlısı sanal asistanınım. Sana yardımcı olmak için buradayım. Konuşmak için bana dokunman yeterli. Haydi sohbet edelim!",
            f"Hoş geldin {self.childName}, ben senin sanal asistanınım. Sana yardımcı olmak için buradayım. Konuşmak için bana dokunman yeterli. Haydi sohbet edelim!",
            f"Selam {self.childName}, ben senin arkadaş canlısı sanal asistanınım. Sana yardımcı olmak için buradayım. Konuşmak için bana dokunman yeterli. Haydi sohbet edelim!",
        ]
        return _initialSentences[Random.randint(1, len(_initialSentences) - 1)]
    

    def greatings(self):
        _greatings = [
            f"Hoşgeldin {self.childName}.",
            f"Merhaba {self.childName}.",
            f"Tekrar hoş geldin {self.childName}.",
            f"Seni tekrar görmek ne güzel {self.childName}.",
            f"Selamlar {self.childName}.",
        ]
        return _greatings[Random.randint(1, len(_greatings) - 1)]
        
    def greatingResponses(self):
        nasilsin = [
            "İyiyim ben de teşekkür ederim.",
            "İyiyim, teşekkür ederim.",
            "Ben de iyiyim, teşekkür ederim.",
            "Tanıştığımıza memnun oldum.",
        ]
        return nasilsin[Random.randint(1, len(nasilsin) - 1)]
    
    def feedback(self):
        _feedbacks = [
            "Harika!",
            "Çok güzel!",
            "Çok iyi!",
            "Çok hoş!",
            "Çok güzel!",
            "Pekala!",
            "Harika tercih!",
        ]
        return _feedbacks[Random.randint(1, len(_feedbacks) - 1)]

    def unexpectedMessage(self):
        _responses = [
            "Üzgünüm, şu anki aşamada spesifik sorulara cevap veremiyorum.",
            "Maalesef ki spesifik sorulara cevap veremiyorum.",
            "Pardon, şu aşamada spesifik sorulara cevap veremiyorum ne yazık ki.",
            "Üzgünüm ki spesifik sorulara cevap veremiyorum.",
        ]
        return _responses[Random.randint(1, len(_responses) - 1)]
    
    def questions(self):
        elderConvs = json.loads(self.elderConversations)
        questions = [
            [
                "Günün nasıldı?",
                "Bugün yaptığın en havalı şey neydi?",
                "Bugün öğrendiğin en güzel şey neydi?",
                "Yarın için planların var mı?",
                "Bugün en çok neyi sevdin?",
                "Bugün en çok neyi sevmedin?",
                "Bugün en çok neyi özledin?",
                "Bugün yaşadığın en komik şey neydi?",
                "Bugün yapmak isteyip de yapamadığın bir şey oldu mu?",
                "Bugün önemli bir şey oldu mu?"
            ],

            "Bana en sevdiğin oyuncağından bahset.",
            "Bildiğin en komik fıkra nedir?",
            "Bir maceraya atılabilseydin, nereye giderdin?",
            "Favori bir süper kahramanın var mı? Kim o?",
            "En sevdiğin dondurma aroması nedir?",
            "Sihirli bir değneğin olsa yapacağın ilk şey ne olurdu?",
            "Bana gerçekten çok güldüğün bir zamandan bahset.",
            "En sevdiğin yatmadan önce hikayeniz nedir?",
            "Şarkı söylemeyi sever misin? En sevdiğin şarkıdan bir mısra söyler misin?",
            "Yeni bir oyuncak yapabilseydin, nasıl olurdu?",
            "Çocuk olmanın en iyi yanı nedir?",
            "Nasıl yapılacağını öğrenmek istediğin bir şey var mı? Varsa nedir?",
            "Favori arkadaşın ya da arkadaşların var mı? Varsa isimleri nelerdir?",
            "Okulda en sevdiğin ders nedir?",
            "En sevdiğin yemek nedir?",
            "Bir hayvan olabilseydin hangisini seçerdin?",
            "En sevdiğin renk nedir?",
            "En sevdiğin oyun nedir?",
            "En sevdiğin spor nedir?",
            "En sevdiğin kitap nedir?",
            "En sevdiğin film nedir?",
            "En sevdiğin çizgi film nedir?",
            "En sevdiğin şarkı nedir?",
            "En sevdiğin mevsim nedir?",
            "En sevdiğin hava durumu hangisidir?",
            "En sevdiğin meyve nedir?",
            "En sevdiğin sebze nedir?",
            "En sevdiğin tatlı nedir?",
            "En sevdiğin içecek nedir?",
            "En sevdiğin çiçek nedir?",
            "En sevdiğin ülke hangisi?",
            "En sevdiğin şehir hangisi?",
            "En sevdiğin yer neresidir?",
        ]
        
        length = len(questions)
        while True:
            isAsked = False
            randomQuestion = Random.randint(1, length - 1)
            if (randomQuestion == 0):
                return questions[0][Random.randint(1, len(questions[0]) - 1)]
            else:
                for conv in elderConvs:
                    message = ""
                    try:
                        message = conv["bot_message"].split("! ")[1]
                    except:
                        message = conv["bot_message"].split(". ")[-1]

                    print()
                    print(message)
                    print(questions[randomQuestion])
                    print()

                    if (questions[randomQuestion] == message):
                        print("Question is asked before")
                        askedQuestion = questions[randomQuestion]
                        questions.remove(askedQuestion)
                        length -= 1
                        isAsked = True
                        break

                if (isAsked == False):
                    return questions[randomQuestion]
                
                if (length == 1):
                    return self.everyDayQuestions()


    def everyDayQuestions(self):
            questions = [
                "Günün nasıldı?",
                "Bugün yaptığın en havalı şey neydi?",
                "Bugün öğrendiğin en güzel şey neydi?",
                "Yarın için planların var mı?",
                "Bugün en çok neyi sevdin?",
                "Bugün en çok neyi sevmedin?",
                "Bugün en çok neyi özledin?",
                "Bugün yaşadığın en komik şey neydi?",
                "Bugün yapmak isteyip de yapamadığın bir şey oldu mu?",
                "Bugün önemli bir şey oldu mu?"
            ]
            
            return questions[Random.randint(1, len(questions) - 1)]
    