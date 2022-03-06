# mengimpor modul individual dari paket,
import sound.effects.echo

# memuat submodule sound.effects.echo.
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

# Cara alternatif untuk mengimpor submodule 
from sound.effects import echo

# memuat submodule echo, dan membuatnya tersedia tanpa awalan paketnya
echo.echofilter(input, output, delay=0.7, atten=4)

# mengimpor fungsi atau variabel yang diinginkan secara langsung
from sound.effects.echo import echofilter

# memuat submodule echo, tetapi ini membuat fungsinya echofilter()tersedia secara langsung
echofilter(input, output, delay=0.7, atten=4)