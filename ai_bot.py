class VirtualAssistant:
    questions = []
    def _init_(self):
        self.questions = [
            "Merhaba! Günün nasıldı?",
            "Bugün yaptığın en havalı şey neydi?",
            "Herhangi bir hayvan olabilseydin hangisini seçerdin?",
            "Bana en sevdiğin oyuncağından bahset.",
            "Bildiğin en komik fıkra nedir?",
            "Bir maceraya atılabilseydin, nereye giderdin?",
            "Favori bir süper kahramanın var mı? Kim o?",
            "En sevdiğiniz dondurma aroması nedir?",
            "Sihirli bir değneğiniz olsa yapacağınız ilk şey nedir?",
            "Bana gerçekten çok güldüğün bir zamandan bahset.",
            "En sevdiğiniz yatmadan önce hikayeniz nedir?",
            "Şarkı söylemeyi sever misin? En sevdiğin şarkıdan bir mısra söyler misin?",
            "Yeni bir oyuncak yapabilseydin, nasıl olurdu?",
            "Çocuk olmanın en iyi yanı nedir?",
            "Nasıl yapılacağını öğrenmek istediğin bir şey nedir?"
        ]
        self.responses = {}

    def chat_with_child(self):
        print("Merhaba! Ben senin arkadaş canlısı sanal asistanınım. Hadi eğlenceli bir sohbet edelim!")
        print("Düşüncelerinizi benimle paylaşmaktan çekinmeyin.")
        for question in self.questions:
            response = input(question + " ")
            self.responses[question] = response
            if "bay" in response.lower():
                print("Güle güle! Seninle konuşmak güzeldi.")
                break
            self.respond_to_answer(response)
        print("Sohbetimiz bitti. İyi günler!")

    def respond_to_answer(self, answer):
        if "okul" in answer.lower():
            print("Okul kulağa heyecan verici geliyor! Favori konunuz nedir?")
        elif "arkadaşlar" in answer.lower():
            print("Arkadaşlar harika! Bana en iyi arkadaşından bahset.")
        elif "süper kahraman" in answer.lower():
            print("Süper kahramanlar çok havalı! Hangi süper gücü isterdin?")
        elif "dondurma" in answer.lower():
            print("Lezzetli! Başka hangi yemekleri yemekten hoşlanırsın?")
        elif "sihirli değnek" in answer.lower():
            print("Sihirli bir değnek harika olurdu! Ne için kullanırdın?")
        elif "uyku zamanı hikayesi" in answer.lower():
            print("Uyku zamanı hikayeleri en iyisidir! Favorini paylaşabilir misin?")
        elif "öğrenmek" in answer.lower():
            print("Yeni şeyler öğrenmek harika! Merak ettiğin bir şey nedir?")
        else:
            print("İlginç! Bana daha fazlasını anlatır mısın?")
    
    def respond_to_answer(self, answer):
        if "hayır" in answer.lower() or "değil" in answer.lower():
            print("Anlıyorum. Eğer böyle hissediyorsan sorun değil.")
        else:
            print("İlginç! Bana daha fazlasını anlatır mısın?")


assistant = VirtualAssistant()
print(assistant.questions)
assistant.chat_with_child()