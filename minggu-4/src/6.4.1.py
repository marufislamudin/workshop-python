# mengimpor tiga submodul yang bernama dari paket tersebut.from sound.effects import *sound
__all__ = ["echo", "surround", "reverse"]

#modul echoand surrounddiimpor ke namespace 
# saat ini karena mereka didefinisikan dalam 
# sound.effectspaket saat 
# from...import pernyataan dijalankan.
import sound.effects.echo
import sound.effects.surround
from sound.effects import *
