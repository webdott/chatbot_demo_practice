knowledge_base = {
    "bàbá": "Bàbá jẹ òbí ọkunrin",
    "ìyá": "Ìyá jẹ òbí obinrin",
    "òkó": "Ọkọ jẹ okunrin olori ile",
    "akọ": "Okunrin jẹ ọkunrin tabi ọkunrin.",
    "abọ": "Obinrin jẹ obinrin tabi obinrin.",
    "tọkọtaya": "tọkọtaya jẹ ìkan ninu àwọn ti wọn se ìgbéyàwó.",
    "àná": "àná je ibatan lokolaya",
    "ebí": "ebí je awon ara-ile eniyan ",
    "òbí": "Ẹniyan ti o bi ọmọ",
    "ọmọ": "Omo jẹ ọmọkan ti o wa niwaju iwaju ọmọpa.",
    "eniyan": "Ẹni jẹ ẹniyan ti a fẹran lọ lati jẹ.",
    "ẹniyan": "Ẹniyan jẹ ọkunrin, obinrin, tabi ọmọ.",
    "igbeyawo": "fifi omo obinrin fun omo okunrin lati fe.",
}

def chat():
    while True:
        user_input = input("User: ")
        if user_input.lower().startswith("ẹnlẹ"):
            print("Chatbot: Ẹ káàbọ! Kí ni o fẹ mọ́ nípa lọ́wọ́ ọjọ́ kan?")
            continue
        if user_input.lower().startswith("o dabo") or user_input.lower().startswith("adupe"):
            print("Chatbot: O dabo! Kú àárọ̀!")
            break
        if (user_input.lower().startswith('kíni') or user_input.lower().startswith('tani')) and user_input.endswith('?'):
            keyword = user_input.rstrip('?').lower().split(' ')[-1];
            if keyword in knowledge_base:
                print("Chatbot:", knowledge_base[keyword])
            else:
                print("Chatbot: Ma binu, mi kò mọ ìtọsọna rẹ.")
        elif user_input.lower().endswith('?'):
            print("Chatbot:", "Ma binu, mi o ni idaun si ibeere ti o bere, jòwó bere ibeere miran")
        else:
            print("Chatbot:", "Mi o mọ bi ma se daùn si ibeere yẹn, jòwó tun ibeere naa ko.")

chat();