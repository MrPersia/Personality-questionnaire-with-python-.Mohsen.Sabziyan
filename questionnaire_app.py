import streamlit as st
import matplotlib.pyplot as plt

def show_instructions(language):
    if language == "Deutsch":
        st.write("Bitte bewerten Sie jede Aussage auf einer Skala von 1 bis 5:")
        st.write("1 - Gar nicht")
        st.write("2 - Kaum")
        st.write("3 - Etwas")
        st.write("4 - Gut")
        st.write("5 - Voll und Ganz")
        st.write("(Bewegen Sie den Schieberegler, um Ihre Bewertung auszuwählen)")
    elif language == "English":
        st.write("Please rate each statement on a scale of 1 to 5:")
        st.write("1 - Not at all")
        st.write("2 - Hardly")
        st.write("3 - Somewhat")
        st.write("4 - Good")
        st.write("5 - Fully")
        st.write("(Use the slider to select your rating)")


def get_responses(fragen):
    antworten = {}
    form = st.form(key='my_form')
    for frage in fragen:
        antworten[frage] = form.slider(frage, 1, 5, key=frage)
    submit_button = form.form_submit_button("Submit")
    
    if submit_button:
        # Validierung der Eingaben
        valid = all(1 <= antworten[frage] <= 5 for frage in fragen)
        if not valid:
            st.error("Bitte bewerten Sie jede Aussage auf einer Skala von 1 bis 5.")
            return None
        return antworten
    return None
    
def assign_categories(antworten, kategorien):
    ergebnisse = {}
    for k, fragen in kategorien.items():
        ergebnisse[k] = sum(antworten[frage] for frage in fragen)
    return ergebnisse

import seaborn as sns

def plot_results(ergebnisse):
    plt.figure(figsize=(12, 8))
    colors = []
    for v in ergebnisse.values():
        if v < 30:
            colors.append("green")
        elif v < 40:
            colors.append("orange")
        else:
            colors.append("red")
    bars = plt.bar(ergebnisse.keys(), ergebnisse.values(), color=colors)
    plt.title('Testergebnisse nach Kategorien')
    plt.xlabel('Kategorie')
    plt.ylabel('Punkte')
    plt.ylim(0, 50)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    for bar, v in zip(bars, ergebnisse.values()):
        plt.text(bar.get_x() + bar.get_width()/2, v + 1, str(v), ha='center', va='bottom')
    st.pyplot(plt)

def evaluate_results(ergebnisse, language):
    if language == "Deutsch":
        st.write("Auswertung für jede Kategorie:")
        for k, v in ergebnisse.items():
            auswertung = ""
            if v < 30:
                auswertung = "förderlich"
                color = "green"
                tip = "Weiter so!"
            elif v < 40:
                auswertung = "mögliche Leistungsbeeinträchtigung"
                color = "orange"
                tip = "Versuchen Sie, in diesem Bereich etwas zu verbessern."
            else:
                auswertung = "möglicherweise gesundheitsgefährdend"
                color = "red"
                tip = "Es könnte wichtig sein, in diesem Bereich Unterstützung zu suchen."
            st.write(f"{k}: {v} Punkte - Auswertung: <span style='color:{color}'>{auswertung}</span> - Tipp: {tip}", unsafe_allow_html=True)
    elif language == "English":
        st.write("Evaluation for every category:")
        for k, v in ergebnisse.items():
            evaluation = ""
            if v < 30:
                evaluation = "Encouraging"
                color = "green"
                tip = "Keep it up!"
            elif v < 40:
                evaluation = "Potential Performance Impairment"
                color = "orange"
                tip = "Try to improve in this area."
            else:
                evaluation = "Possibly Health Hazardous"
                color = "red"
                tip = "It might be important to seek support in this area."
            st.write(f"{k}: {v} Points - Evaluation: <span style='color:{color}'>{evaluation}</span> - Tip: {tip}", unsafe_allow_html=True)


def get_questions_and_categories(language):
    if language == "Deutsch":
        fragen = [
            "Wann immer ich eine Arbeit mache, dann mache ich sie gründlich.",
            "Ich fühle mich verantwortlich, dass diejenigen, „die mit mir zu tun“ haben, sich wohlfühlen.",
            "Ich bin ständig auf Trab.",
            "Wenn ich raste, roste ich.",
            "Anderen gegenüber zeige ich meine Schwächen nicht gerne.",
            "Häufig gebrauche ich den Satz: „Es ist schwierig, etwas so genau zu sagen.“",
            "Ich sage oft mehr, als eigentlich nötig wäre.",
            "Ich habe Mühe, Leute zu akzeptieren, die nicht genau sind.",
            "Es fällt mir schwer, Gefühle zu zeigen.",
            "„Nur nicht lockerlassen“, ist meine Devise.",
            "Wenn ich eine Meinung äußere, begründe ich sie auch.",
            "Wenn ich einen Wunsch habe, erfülle ich ihn mir schnell.",
            "Ich liefere einen Bericht erst ab, wenn ich ihn mehrere Male überarbeitet habe.",
            "Leute, die „herumtrödeln“, regen mich auf.",
            "Es ist für mich wichtig, von anderen akzeptiert zu werden.",
            "Ich habe eher eine harte Schale, aber einen weichen Kern.",
            "Ich versuche oft herauszufinden, was andere von mir erwarten, um mich danach zu richten.",
            "Leute, die unbekümmert in den Tag hineinleben, kann ich nur schwer verstehen.",
            "Bei Diskussionen unterbreche ich die anderen oft.",
            "Ich löse meine Probleme selber.",
            "Aufgaben erledige ich möglichst rasch.",
            "Im Umgang mit anderen bin ich auf Distanz bedacht.",
            "Ich sollte viele Aufgaben noch besser erledigen.",
            "Ich kümmere mich persönlich auch um nebensächliche Dinge.",
            "Erfolge fallen nicht vom Himmel, ich muss sie hart erarbeiten.",
            "Für dumme Fehler habe ich wenig Verständnis.",
            "Ich schätze es, wenn andere meine Fragen rasch und bündig beantworten.",
            "Es ist mir wichtig, von anderen zu erfahren, ob ich meine Sache gut gemacht habe.",
            "Wenn ich eine Aufgabe einmal begonnen habe, führe ich sie auch zu Ende.",
            "Ich stelle meine Wünsche und Bedürfnisse zugunsten der Bedürfnisse anderer Personen zurück.",
            "Ich bin anderen gegenüber oft hart, um von ihnen nicht verletzt zu werden.",
            "Ich trommle oft ungeduldig mit den Fingern auf den Tisch (ich bin ungeduldig).",
            "Beim Erklären von Sachverhalten verwende ich gerne die klare Aufzählung: erstens..., zweitens..., drittens...",
            "Ich glaube, dass die meisten Dinge nicht so einfach sind, wie viele meinen.",
            "Es ist mir unangenehm, andere Leute zu kritisieren.",
            "Bei Diskussionen nicke ich häufig mit dem Kopf.",
            "Ich strenge mich an, um meine Ziele zu erreichen.",
            "Mein Gesichtsausdruck ist eher ernst.",
            "Ich bin nervös.",
            "So schnell kann mich nichts erschüttern.",
            "Meine Probleme gehen die anderen nichts an.",
            "Ich sage oft: „Tempo, Tempo, das muss rascher gehen!“",
            "Ich sage oft: „genau“, „exakt“, „klar“, „logisch“, o.ä.",
            "Ich sage oft: „Das verstehe ich nicht...“",
            "Ich sage gerne: „Könnten Sie es nicht einmal versuchen?“ und sage nicht gerne: „Versuchen Sie es einmal.“",
            "Ich bin diplomatisch.",
            "Ich versuche, die an mich gestellten Erwartungen zu übertreffen.",
            "Ich mache manchmal zwei Tätigkeiten gleichzeitig.",
            "„Die Zähne zusammenbeißen“ heißt meine Devise.",
            "Trotz enormer Anstrengungen will mir vieles einfach nicht gelingen."
        ]
        kategorien = {
            'Sei perfekt': [
                "Wann immer ich eine Arbeit mache, dann mache ich sie gründlich.",
                "Ich habe Mühe, Leute zu akzeptieren, die nicht genau sind.",
                "Wenn ich eine Meinung äußere, begründe ich sie auch.",
                "Ich liefere einen Bericht erst ab, wenn ich ihn mehrere Male überarbeitet habe.",
                "Ich sollte viele Aufgaben noch besser erledigen.",
                "Ich kümmere mich persönlich auch um nebensächliche Dinge.",
                "Beim Erklären von Sachverhalten verwende ich gerne die klare Aufzählung: erstens..., zweitens..., drittens...",
                "Mein Gesichtsausdruck ist eher ernst.",
                "Ich sage oft: „genau“, „exakt“, „klar“, „logisch“, o.ä.",
                "Ich versuche, die an mich gestellten Erwartungen zu übertreffen."
            ],
            'Mach schnell': [
                "Ich bin ständig auf Trab.",
                "Wenn ich einen Wunsch habe, erfülle ich ihn mir schnell.",
                "Leute, die „herumtrödeln“, regen mich auf.",
                "Ich löse meine Probleme selber.",
                "Aufgaben erledige ich möglichst rasch.",
                "Ich schätze es, wenn andere meine Fragen rasch und bündig beantworten.",
                "Ich trommle oft ungeduldig mit den Fingern auf den Tisch (ich bin ungeduldig).",
                "Ich bin nervös.",
                "Ich sage oft: „Tempo, Tempo, das muss rascher gehen!“",
                "Ich mache manchmal zwei Tätigkeiten gleichzeitig."
            ],
            'Streng dich an': [
                "Wenn ich raste, roste ich.",
                "Häufig gebrauche ich den Satz: „Es ist schwierig, etwas so genau zu sagen.“",
                "„Nur nicht lockerlassen“, ist meine Devise.",
                "Leute, die unbekümmert in den Tag hineinleben, kann ich nur schwer verstehen.",
                "Erfolge fallen nicht vom Himmel, ich muss sie hart erarbeiten.",
                "Wenn ich eine Aufgabe einmal begonnen habe, führe ich sie auch zu Ende.",
                "Ich glaube, dass die meisten Dinge nicht so einfach sind, wie viele meinen.",
                "Ich strenge mich an, um meine Ziele zu erreichen.",
                "Ich sage oft: „Das verstehe ich nicht...“",
                "Trotz enormer Anstrengungen will mir vieles einfach nicht gelingen."
            ],
            'Mach es allen Recht': [
                "Ich fühle mich verantwortlich, dass diejenigen, „die mit mir zu tun“ haben, sich wohlfühlen.",
                "Ich sage oft mehr, als eigentlich nötig wäre.",
                "Es ist für mich wichtig, von anderen akzeptiert zu werden.",
                "Ich versuche oft herauszufinden, was andere von mir erwarten, um mich danach zu richten.",
                "Es ist mir wichtig, von anderen zu erfahren, ob ich meine Sache gut gemacht habe.",
                "Ich stelle meine Wünsche und Bedürfnisse zugunsten der Bedürfnisse anderer Personen zurück.",
                "Es ist mir unangenehm, andere Leute zu kritisieren.",
                "Bei Diskussionen nicke ich häufig mit dem Kopf.",
                "Ich sage gerne: „Könnten Sie es nicht einmal versuchen?“ und sage nicht gerne: „Versuchen Sie es einmal.“",
                "Ich bin diplomatisch."
            ],
            'Sei stark': [
                "Anderen gegenüber zeige ich meine Schwächen nicht gerne.",
                "Es fällt mir schwer, Gefühle zu zeigen.",
                "Ich habe eher eine harte Schale, aber einen weichen Kern.",
                "Bei Diskussionen unterbreche ich die anderen oft.",
                "Meine Probleme gehen die anderen nichts an.",
                "Für dumme Fehler habe ich wenig Verständnis.",
                "Ich bin anderen gegenüber oft hart, um von ihnen nicht verletzt zu werden.",
                "So schnell kann mich nichts erschüttern.",
                "Meine Probleme gehen die anderen nichts an.",
                "„Die Zähne zusammenbeißen“ heißt meine Devise."
            ]
        }
    elif language == "English":
        fragen = [
            "I always do a thorough job whenever I undertake something.",
            "I feel responsible for making sure that those I come in contact with are comfortable.",
            "I am always on the go.",
            "If I rest, I rust.",
            "I don't like to show my weaknesses to others.",
            "I often use the phrase: 'It's difficult to say something so precisely.'",
            "I often say more than is really necessary.",
            "I have trouble accepting people who are not exact.",
            "It is difficult for me to show feelings.",
            "'Never give up' is my motto.",
            "When I express an opinion, I also give reasons for it.",
            "When I have a wish, I fulfill it quickly.",
            "I only deliver a report after I have revised it several times.",
            "I get annoyed by people who 'dawdle'.",
            "It is important for me to be accepted by others.",
            "I have a tough outer shell, but a soft core.",
            "I often try to figure out what others expect of me in order to adapt to it.",
            "I find it difficult to understand people who live carefree lives.",
            "I often interrupt others in discussions.",
            "I solve my problems on my own.",
            "I try to complete tasks as quickly as possible.",
            "I am cautious about keeping my distance from others.",
            "I should do many tasks even better.",
            "I also take care of trivial matters personally.",
            "Successes don't come from nowhere, I have to work hard for them.",
            "I have little understanding for stupid mistakes.",
            "I appreciate it when others answer my questions quickly and to the point.",
            "It is important for me to find out from others whether I have done my job well.",
            "Once I have started a task, I also finish it.",
            "I put my wishes and needs aside in favor of the needs of other people.",
            "I am often tough on others so as not to be hurt by them.",
            "I often drum impatiently with my fingers on the table (I am impatient).",
            "When explaining facts, I like to use a clear enumeration: first..., second..., third...",
            "I believe that most things are not as simple as many people think.",
            "It makes me uncomfortable to criticize other people.",
            "I often nod my head in discussions.",
            "I strive to achieve my goals.",
            "My facial expression is rather serious.",
            "I am nervous.",
            "Nothing can shake me quickly.",
            "My problems are none of others' business.",
            "I often say: 'Hurry, hurry, it needs to be faster!'",
            "I often say: 'exactly', 'precisely', 'clear', 'logical', etc.",
            "I often say: 'I don't understand this...' ",
            "I like to say: 'Can't you at least try?' and don't like to say: 'Try it.'",
            "I am diplomatic.",
            "I try to exceed the expectations placed on me.",
            "I sometimes do two things at the same time.",
            "'Grit your teeth' is my motto.",
            "Despite enormous efforts, many things simply don't work out for me."
        ]
        kategorien = {
            'Be perfect': [
                "I always do a thorough job whenever I undertake something.",
                "I have trouble accepting people who are not exact.",
                "When I express an opinion, I also give reasons for it.",
                "I only deliver a report after I have revised it several times.",
                "I should do many tasks even better.",
                "I also take care of trivial matters personally.",
                "When explaining facts, I like to use a clear enumeration: first..., second..., third...",
                "My facial expression is rather serious.",
                "I often say: 'exactly', 'precisely', 'clear', 'logical', etc.",
                "I try to exceed the expectations placed on me."
            ],
            'Act quickly': [
                "I am always on the go.",
                "When I have a wish, I fulfill it quickly.",
                "I get annoyed by people who 'dawdle'.",
                "I solve my problems on my own.",
                "I try to complete tasks as quickly as possible.",
                "I appreciate it when others answer my questions quickly and to the point.",
                "I often drum impatiently with my fingers on the table (I am impatient).",
                "I am nervous.",
                "I often say: 'Hurry, hurry, it needs to be faster!'",
                "I sometimes do two things at the same time."
            ],
            'Strive hard': [
                "If I rest, I rust.",
                "I often use the phrase: 'It's difficult to say something so precisely.'",
                "'Never give up' is my motto.",
                "I find it difficult to understand people who live carefree lives.",
                "Successes don't come from nowhere, I have to work hard for them.",
                "Once I have started a task, I also finish it.",
                "I believe that most things are not as simple as many people think.",
                "I strive to achieve my goals.",
                "I often say: 'I don't understand this...' ",
                "Despite enormous efforts, many things simply don't work out for me."
            ],
            'Please everyone': [
                "I feel responsible for making sure that those I come in contact with are comfortable.",
                "I often say more than is really necessary.",
                "It is important for me to be accepted by others.",
                "I often try to figure out what others expect of me in order to adapt to it.",
                "It is important for me to find out from others whether I have done my job well.",
                "I put my wishes and needs aside in favor of the needs of other people.",
                "It makes me uncomfortable to criticize other people.",
                "I often nod my head in discussions.",
                "I like to say: 'Can't you at least try?' and don't like to say: 'Try it.'",
                "I am diplomatic."
            ],
            'Be strong': [
                "I don't like to show my weaknesses to others.",
                "It is difficult for me to show feelings.",
                "I have a tough outer shell, but a soft core.",
                "I often interrupt others in discussions.",
                "My problems are none of others' business.",
                "I have little understanding for stupid mistakes.",
                "I am often tough on others so as not to be hurt by them.",
                "Nothing can shake me quickly.",
                "My problems are none of others' business.",
                "'Grit your teeth' is my motto."
            ]
        }
    return fragen, kategorien

def questionnaire_app():
    st.title("Personality Questionnaire")

    language = st.selectbox("Choose language:", ["English", "Deutsch"])

    fragen, kategorien = get_questions_and_categories(language)
    show_instructions(language)
    antworten = get_responses(fragen)
    if antworten is not None:
        ergebnisse = assign_categories(antworten, kategorien)
        evaluate_results(ergebnisse, language)
        plot_results(ergebnisse)

if __name__ == "__main__":
    questionnaire_app()
