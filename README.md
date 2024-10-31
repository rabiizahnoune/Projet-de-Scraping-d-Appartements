**Projet de Scraping d'Appartements**

*Ce projet utilise Selenium pour scraper des liens et des données d'appartements sur le site Avito et les stocke dans des fichiers texte et CSV. Il est divisé en trois fichiers principaux : scarper.py, utils.py, et execute.py*


**Structure du Projet**

***scarper.py***: Contient les classes ApartmentLinkScraper et ApartmentDataScraper.

***ApartmentLinkScraper*** : Scrape les liens des appartements en parcourant plusieurs pages de recherche sur Avito.
***ApartmentDataScraper*** : Utilise les liens collectés pour extraire des informations comme le titre, le prix, la localisation, le nombre de chambres, etc.
***utils.py*** : Contient la classe WebScraperUtils qui facilite les opérations courantes de scraping, comme la gestion du driver Selenium et la récupération sécurisée des éléments.

*** execute.py ***: Script principal qui utilise les classes définies dans scarper.py pour lancer le scraping et enregistrer les résultats.




**Installation**
1/Cloner le projet
2/Installer les dépendances avec : pip install -r requirements.txt



