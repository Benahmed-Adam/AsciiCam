# AsciiCam

Ce projet est un moteur de rendu en **ASCII Art** qui transforme un flux vidéo (webcam ou fichier vidéo) en une matrice de caractères directement dans le terminal. Il est également possible d’activer un rendu en couleur et de synchroniser le son de la vidéo.

## Fonctionnalités

* Lecture en temps réel via la webcam
* Lecture de fichiers vidéo avec restitution audio synchronisée
* Conversion pixel → caractère ASCII en niveaux de gris ou en couleur
* Optimisation du rendu grâce à un rafraîchissement différentiel (seules les zones modifiées sont mises à jour)
* Limitation du framerate pour respecter le FPS d’origine

## Dépendances

Avant d’exécuter le script, installez les bibliothèques nécessaires :

```bash
pip install pillow opencv-python numpy pygame moviepy
```

## Structure du projet

* **ascii\_renderer** : classe principale qui gère l’acquisition vidéo, la conversion en ASCII et l’affichage dans le terminal
* **Modes** :

  * `cam` : capture en direct via la webcam
  * `vid` : lecture d’un fichier vidéo avec extraction et lecture de la piste audio

## Utilisation

### 1. Webcam

```python
from asciiRenderer import ascii_renderer

renderer = ascii_renderer("cam", couleur=True, opti=True)
renderer.run()
```

### 2. Vidéo locale

```python
from asciiRenderer import ascii_renderer

renderer = ascii_renderer("vid", couleur=False, opti=True)
renderer.run()
```

Lors du choix du mode `vid`, le programme demande le chemin de la vidéo (par exemple `video.mp4`).

## Paramètres

* **mode** : `"cam"` ou `"vid"`
* **couleur** (`bool`) :

  * `False` → rendu ASCII en niveaux de gris
  * `True` → rendu ASCII en couleur

Exemple :

```python
renderer = ascii_renderer("vid", couleur=True, opti=True)
```

## Notes

* Le rendu dépend de la taille du terminal (`os.get_terminal_size`)
* Pour de meilleures performances, utilisez un terminal en plein écran
* Ne pas redimensionner le terminal, lors du rendu sous peine de crash
* Le rendu peut varier selon la résolution choisie et la taille du terminal
