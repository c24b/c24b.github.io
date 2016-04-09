# Tutoriel
## Notre premier crawl ciblé
Ici nous allons créer pour l'exmple un crawl ciblé autour 
des prises de paroles en ligne sur la loi travail

Pour cela  nous allons créer le projet loi_travail
  ```name: "loi_travail"```

Pour un crawl ciblé autour d'une thématique nous avons besoin
d'une expression de recherche que nous devons définir avec soin
elle ne doit être ni trop large ni trop étroite pour permettre au crawler 
de collecter les informations sur la polémiques


Nous allons modifier dans la fichier la "query":
  ```
  "query":{
  
            "active": true, 
            "query": "loi AND (Travail OR El K?omri)" 
            }
  ```
Plus de détails sur les expressions de recherche et leur syntaxe: Glossaire


Au vu du bruit médiatique autour de ce sujet nous allons limiter
la  profondeur du crawl à 3 soit le résultats des recherches + 2 niveaux
pour ne pas surcharger le crawler

 ```
 depth:{
         "active": true, 
         "depth":3
         },     
```
Plus de détails sur la profondeur d'uncrawl: Glossaire

Le contenu qui nous intéresse est en français et on désire filtrer la langue cible
 ```
 "lang":{
         "active": true, 
         "lang":"fr",
         },     
```
Plus de détails sur les langues supportées: Glossaire

Le crawl doit partir d'une recherche initiale sur BING
nous allons modifier la partie seeds
* ajouter la clé d'API pour activer la recherche en ligne
* mettre le nombre de résultats que nous voulons récupérer (50)
* et désactiver les autres options en mettat à false

Plus de détails sur le fonctionnement de recherche sur Bing: Glossaire
```
"seeds": {
        "url":{
            "active": false,
            "url": ""
            },
        "file":{
            "active": false,
            "file": ""
            },
        "search": {
            "active": true,
            "key": "J8zre1019v/dIT0oXXXXXXXXX",
            "nb": 50
            }
        }```

Le crawl sera répété toutes les semaines (exprimées en jour)
"scheduler": {
        "active": true,
        "days": 7
    },

Plus de détails sur les routines: Glossaire
    
La configuration de otre crawl prend donc cette forme:
```
{
    "name": "loi_travail",
    "filters": {
        "depth":{ 
            "active": true,
            "depth": 3
            },
        "lang":{
            "active": true,
            "lang": "fr"
            },
        "query":{
            "active": true,
            "query": "Loi AND (travail OR el khomri)"
            }
    },
    "scheduler": {
        "active": true,
        "days": 30
    },
    "seeds": {
        "url":{
            "active": false,
            "url": ""
            },
        "file":{
            "active": false,
            "file": ""
            },
        "search": {
            "active": true,
            "key": "MyApiSECRETKeydIT0o",
            "nb": 50
            }
        }
}

```
 Enregistrons le au même endroit dans un fichier final appelé loi_travail.json 
Nous allons maintenant charger la configuration 

Ouvrons le terminal activons le virtual env et déplacons nous jusqu'aux fichiers sources de crawtext
```
(venv) me@ordi:$~ cd crawtext
(venv) me@ordi:$~/crawtext/ python crawtext setup --project=loi_travail
```
Il suffit maintenant de le lancer en utilisant la comande start
```
(venv) me@ordi:$~ 
(venv) me@ordi:$~/crawtext/ python crawtext start --project=loi_travail
```
 Le crawl a commencé et durera tant qu'il aura des pages pertinentes à traiter





