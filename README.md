# HTPA32x32d Capture Image

## Projenin amacı
Raspberry pi ile beraber HTPA32x32d 'den görüntü almak.
## Gereksinimler
### Raspberry pi Konfigurasyonu
İlk olarak I2C ayarlarını yapıyoruz.
#### [I2C'yi Yapılandırma](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c)

Konsolu açtıktan sonra `Sudo raspi-config` yazalım.

Ardından aşağıdaki adımları takip edelim.
    			<img src="Markdown/images/learn_raspberry_pi_interfacing.png">
                <img src="Markdown/images/learn_raspberry_pi_advancedopt.png">
                <img src="Markdown/images/learn_raspberry_pi_i2c.png">
                <img src="Markdown/images/learn_raspberry_pi_wouldyoukindly.png">
                <img src="Markdown/images/learn_raspberry_pi_i2ckernel.png">
Cihazın bağlantılı olup olmadığını görmek için `sudo apt-get install -y i2c-tools' kütüphanesini indirin ve konsola    `sudo i2cdetect -y 1` yazın eğer birinci kanalı kullanmıyorsanız 0-2-3 gibi kanallarada bakabilirsiniz.            
           
                <img src="Markdown/images/learn_raspberry_pi_i2c-detect.png">
                
                
## Kod İçeriği
## Çıktılar
## Yaşanılan Problemler
## Ekstra Bilgiler
