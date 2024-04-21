Login: Ján Findra (xfindr01)  
Dátum: 21.4.2024  

# Zmena oproti 1. časti projektu

## Zmeny v súboroch *.feature

### Zmeny v súbore `product-adding-to-cart.feature`

V scenároch 7. a 8. som zmenil `@given` pridaním `#2`, aby scenáre nekolidovali s predchádzajúcimi.  

```gherkin
Given user is on the result page -> Given user is on the result page #2
```
V scenári 7. som zrušil kontrolu, či bolo zobrazené upozornenie o neúspešnom pridaní produktu do košíka, duplicitná kontrola nie je potrebná.

### Drobné zmeny

Veľa zmien bolo z dôvodu, že zdieľane kroky nemali úplne totožné názvy z dôvodu vynechania predložky alebo zabudnutého písmena.