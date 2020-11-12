# Privacy en Amphi

Cette activité est basée sur une idée originale (disponnible [ici](QuoiProCo.pdf)) de Tristan Allard, Louis Béziaud, Noé Brucy, Joris Duguépéroux et Antonin Voyez proposée au concours EDUCNUM 2017.
Elle est diffusée sous licence CC-BY-SA.

## Objectif

Illustrer la collecte d'informations respectueuse de la vie privée à l'échelle d'un amphithéâtre (plus de personnes = plus de fiabilité).

L'activité permet potentiellement d'obtenir des informations sur des sujets sensibles. Les questions considérées sont fermées (binaires).

- Êtes-vous communiste ? dans le contexte de la Guerre Froide.
- Avez-vous déjà consommé de la drogue ?
- Avez-vous déjà eu recours à l'avortement ?
- Faites-vous encore pipi au lit ?
- Avez-vous triché à un contrôle cette année ?

## Background

On utilise deux outils techniques : la *differential privacy* et *randomized response*.

### Differential privacy

https://www.cis.upenn.edu/~aaroth/Papers/privacybook.pdf

### Randomized response

https://www.dartmouth.edu/~chance/teaching_aids/RResponse/RResponse.html

Pour une question fermée donnée, le répondant a une réponse réelle **privée** `s`. Le questionneur lui pose la question. Avec une probabilité `p < 0.5` le répondant donne au questionneur la réponse réelle `s`, avec une probabilité `1 - p` il ment et répond `not s`.

Le générateur d'aléa peut être un dé (mensonge si tombe sur 6, vérité sinon).

## Déroulé

1. On pose quelques questions banales aux élèves sans *randomized response* pour avoir une statistique de base, "Aimes-tu la gelée de coing ?"
2. On présente le mécanisme de réponse et le contexte (type cours)
3. On repose les questions banales, avec *randomized response*
4. Les résultats des étapes 1 et 3 sont affichés et comparés (avec un peu de chance les 2 sont proches, et on peut même estimer le bruit attendu)
5. On pose des questions gênantes avec *randomized response*, pour avoir des statistiques plus intéressantes à discuter et illustrer l'enjeu

## Collecter des statistiques en amphi

voir [Plickers](https://www.plickers.com/) ou [VotAR](https://libre-innovation.org)
