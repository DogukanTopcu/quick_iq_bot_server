import json
from flask import Flask, request, jsonify
import virtual_assistant as va

app = Flask(__name__)

@app.route('/', methods=['GET'])
def getPage():
    return "Welcome to the virtual assitant server!"


@app.route('/api/generateText', methods=['POST'])
def generateText():
    data = request.get_json()
    elderConvs = json.loads(data["elderConversations"])
    print(len(elderConvs))

    if (elderConvs != []):
        if (data["mode"] == "first"):
            virtual_assistant = va.VirtualAssistant(data['name'], data['elderConversations'])
            return virtual_assistant.greatings() + " " + virtual_assistant.questions()
        else:
            print(data["mode"])
            if ("?" in data["mode"]):
                if ("nasılsın" in data["mode"]):
                    virtual_assistant = va.VirtualAssistant(data['name'], data['elderConversations'])
                    return virtual_assistant.greatingResponses() + " " + virtual_assistant.everyDayQuestions()
                else:
                    virtual_assistant = va.VirtualAssistant(data['name'], data['elderConversations'])
                    return virtual_assistant.unexpectedMessage() + " Ama sorduğum sorularımı cevaplamandan büyük mutluluk duyarım. " + virtual_assistant.questions()
            else:
                virtual_assistant = va.VirtualAssistant(data['name'], data['elderConversations'])
                return virtual_assistant.feedback() + " " + virtual_assistant.questions()

    else:
        virtual_assistant = va.VirtualAssistant(data['name'], data['elderConversations'])
        return virtual_assistant.initialSentences()

if __name__ == '__main__':
    app.run(debug=True, port=6000)