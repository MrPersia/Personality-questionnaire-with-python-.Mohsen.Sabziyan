import streamlit as st
import matplotlib.pyplot as plt

def show_instructions():
    st.write("Bitte bewerten Sie jede Aussage auf einer Skala von 1 bis 5:")
    st.write("1 - Gar nicht")
    st.write("2 - Kaum")
    st.write("3 - Etwas")
    st.write("4 - Gut")
    st.write("5 - Voll und Ganz")

def get_responses(fragen):
    antworten = {}
    form = st.form(key='my_form')
    for frage in fragen:
        antworten[frage] = form.slider(frage, 1, 5, key=frage)
    submit_button = form.form_submit_button("Submit")
    if submit_button:
        return antworten
    return None

def assign_categories(antworten, kategorien):
    ergebnisse = {}
    for k, fragen in kategorien.items():
        ergebnisse[k] = sum(antworten[frage] for frage in fragen)
    return ergebnisse

def plot_results(ergebnisse):
    plt.figure(figsize=(12, 8))
    plt.bar(ergebnisse.keys(), ergebnisse.values(), color='skyblue')
    plt.title('Testergebnisse nach Kategorien')
    plt.xlabel('Kategorie')
    plt.ylabel('Punkte')
    plt.ylim(0, 50)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    for i, (k, v) in enumerate(ergebnisse.items()):
        plt.text(i, v + 1, str(v), ha='center', va='bottom')
    st.pyplot(plt)

def evaluate_results(ergebnisse):
    st.write("Auswertung für jede Kategorie:")
    for k, v in ergebnisse.items():
        auswertung = ""
        auswertung_color = ""
        if v < 30:
            auswertung = "förderlich"
            auswertung_color = "green"
        elif v < 40:
            auswertung = "mögliche Leistungsbeeinträchtigung"
            auswertung_color = "orange"
        else:
            auswertung = "möglicherweise gesundheitsgefährdend"
            auswertung_color = "red"
        st.write(f"{k}: {v} Punkte - Auswertung: ", auswertung, ' ', st.markdown(f"<span style='color:{auswertung_color}'>{auswertung}</span>", unsafe_allow_html=True))

def questionnaire_app():
    st.title("Persönlichkeitsfragebogen")

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

    show_instructions()
    antworten = get_responses(fragen)
    if antworten:
        ergebnisse = assign_categories(antworten, kategorien)
        plot_results(ergebnisse)
        evaluate_results(ergebnisse)

if __name__ == "__main__":
    questionnaire_app()
