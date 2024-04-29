# Personality-questionnaire-with-python-.Mohsen.Sabziyan
# Persönlichkeitsfragebogen

Dies ist eine interaktive Anwendung, die einen Persönlichkeitsfragebogen anbietet. Der Fragebogen basiert auf der Beantwortung einer Reihe von Aussagen und ermöglicht es, die persönlichen Präferenzen und Verhaltensweisen in verschiedenen Bereichen zu bewerten.

## Anwendung

Die Anwendung bietet die Möglichkeit, den Fragebogen in zwei Sprachen, Deutsch und Englisch, zu beantworten. Nachdem die Sprache ausgewählt wurde, werden dem Benutzer eine Reihe von Aussagen präsentiert, die er auf einer Skala von 1 bis 5 bewerten kann, wobei 1 "Gar nicht" und 5 "Voll und ganz" bedeutet. Nachdem alle Aussagen bewertet wurden, werden die Ergebnisse analysiert und die Punkte in verschiedenen Kategorien zusammengefasst.

## Kategorien

Die Fragen sind in fünf Hauptkategorien unterteilt:

- **Sei perfekt**: Bewertet die Neigung, Dinge gründlich zu erledigen und hohe Standards zu setzen.
- **Mach schnell**: Bewerten Sie die Neigung, Dinge schnell zu erledigen und ungeduldig zu sein.
- **Streng dich an**: Bewertet die Neigung, hart zu arbeiten und sich stark zu bemühen, Ziele zu erreichen.
- **Mach es allen Recht**: Bewerten Sie die Neigung, sich um das Wohlergehen anderer zu kümmern und diplomatisch zu sein.
- **Sei stark**: Bewerten Sie die Neigung, sich stark zu zeigen, Emotionen zurückzuhalten und unabhängig zu sein.

## Auswertung

Die Anwendung berechnet die Gesamtpunkte für jede Kategorie und zeigt die Ergebnisse grafisch in einem Diagramm an. Außerdem wird eine Gesamtauswertung basierend auf den Gesamtpunkten der Benutzer präsentiert, die auf drei Ebenen der Persönlichkeitsmerkmale beruht:

- **Förderlich**: Punktzahl unter 30.
- **Mögliche Leistungsbeeinträchtigung**: Punktzahl zwischen 30 und 39.
- **Möglicherweise gesundheitsgefährdend**: Punktzahl über 40.

## Verwendung

Um die Anwendung lokal auszuführen, führen Sie einfach `streamlit run questionnaire_app.py` aus. Stellen Sie sicher, dass Sie die erforderlichen Python-Bibliotheken installiert haben (siehe `requirements.txt`).
