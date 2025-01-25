Les étapes principales incluent l'authentification de l'utilisateur via OAuth 2.0, la récupération d'une liste de chaînes auxquelles l'utilisateur est abonné,
la recherche de vidéos en fonction de chaînes et de mots-clés, puis la collecte des commentaires de l'utilisateur sur ces vidéos.

Le script est conçu pour :

  Authentification de l'utilisateur : Utilise OAuth 2.0 pour authentifier l'utilisateur et renvoyer un client valide pour les interactions ultérieures avec l'API.
  Récupérer les chaînes abonnées : Pour chaque canal de l'utilisateur, il récupère la liste des chaînes auxquelles l'utilisateur est abonné.
  Rechercher des vidéos par chaîne et mots-clés : Le script recherche des vidéos publiées dans les 30 derniers jours sur une liste de chaînes définies, filtrées optionnellement par des mots-clés spécifiques.
  Récupérer les commentaires des vidéos : Une fois les vidéos trouvées, le script récupère les commentaires de ces vidéos écrits par l'utilisateur spécifié.
  Sauvegarder les commentaires dans un fichier : Tous les commentaires récupérés sont sauvegardés dans un fichier texte, en s'assurant que les doublons ne soient pas ajoutés.

Aperçu de l'API YouTube V3 :

L'API YouTube Data V3 permet aux développeurs d'interagir avec YouTube, offrant des actions telles que la récupération des détails de vidéos, des informations sur les chaînes, et des commentaires des utilisateurs. Vous interagissez avec l'API via des requêtes HTTP incluant divers paramètres pour filtrer les résultats.

  ID des vidéos : Les ID des vidéos sur YouTube sont des identifiants uniques pour chaque vidéo sur la plateforme. Ces ID font partie de l'URL de la vidéo (par exemple, dans https://www.youtube.com/watch?v=VIDEO_ID).
  ID des chaînes : Un ID de chaîne identifie de manière unique une chaîne YouTube. Il est utilisé pour interroger des chaînes spécifiques, leurs vidéos, abonnements, et plus encore.
  Authentification OAuth : L'API utilise OAuth 2.0 pour l'authentification, permettant aux utilisateurs d'autoriser l'application à accéder à leurs données.

Méthodes clés de l'API utilisées dans ce script :

  subscriptions().list() : Récupère la liste des abonnements pour une chaîne spécifique.
  search().list() : Recherche des vidéos sur les chaînes, filtrées par mots-clés et date de publication.
  commentThreads().list() : Récupère les commentaires pour une vidéo spécifique.

Remarques Importantes :

  Limitation de Taux : L'API impose des limites de taux, et ce script garde une trace du nombre de requêtes effectuées pour éviter de dépasser ces limites (10K basic)
  Récupération des Commentaires : Les vidéos avec des commentaires désactivés sont automatiquement ignorées.

Dépendances :

  google-auth-oauthlib
  google-api-python-client
