# QuickStart Guide (PL)

## Wymagania sprzętowe

W celu uruchomienia naszej aplikacji, należy spełniąc następujące wymagania sprzętowe:
- Raspberry Pi 4B (używana przez nas wersja posiada 8GB RAM, ale powinno działać na modelach 4GB i nawet 2GB) z Ubuntu Server,
- Konwerter "USB to TTL", który wykorzystywany jest do wysyłania wiadomości do serwomechanizmów,
- Platforma HEXAPOD z silnikami Robotis Dynamixel AX-12A.

---

## Wymagane oprogramowanie

Na komputerze Raspberry Pi należy zainstalować Docker oraz Git
- Instalacja Git:
    ```bash
    sudo apt-get install git -y
    ```
- Instalacja Docker:
    ```bash
    curl -fsSL https://get.docker.com -o get-docker.sh
    chmod +x get-docker.sh 
    sudo apt-get purge docker-ce docker-ce-cli containerd.io -y
    ./get-docker.sh
    # (pi is the user name)
    sudo usermod -aG docker pi
    sudo systemctl unmask docker
    sudo chmod 666 /var/run/docker.sock
    pip3 -v install docker-compose
    sudo systemctl start docker
    # or sudo reboot
    sudo init 6
    ```

---

## Pierwsze uruchomienie programu

Po zainstalowaniu wymaganego oprogramowania, należy wykonać następujące czynności:
- Przejść do wybranego przez siebie katalogu (np. /home/pi/)
    ```bash
    cd /home/pi/
    ```
    lub utworzyć własny w dowolnym miejścu (np. /root/),
    ```bash
    mkdir ~/HEXAPOD/
    ```
- Sklonować zawartość repozytorium za pomocą git
    ```bash
    git clone https://github.com/revalew/HEXAPOD.git
    ```
- Przejść do folderu **docker** w sklonowanym wcześniej repozytorium
    ```bash
    cd ~/HEXAPOD/docker
    ```
- Upewnić się, że konwerter TTL jest podpięty do portu USB i ma adres /dev/ttyUSB0,
    ```bash
    dmesg | grep tty
    ```
    jeżeli konwerter ma inny adres, należy zmienić go na odpowiedni w pliku *docker-compose.yml* w sekcji *devices*.
-  Utworzyć obraz docker zgodnie z instrukcjami pliku *dockerfile*
    ```bash
    docker build -t ros2 .
    ```
    *ros2* to nazwa naszego kontenera.
- Uruchomić nasz nowy kontener z ustawieniami zawartymi w *docker-compose.yml*
    ```bash
    docker-compose up -d
    ```
- Uruchomić interaktywną sesję dla działającego kontenera
    ```bash
    docker exec -it docker_ros2_1 bash
    ```
    jeżeli występuje błąd nazwy (docker_ros2_1 sięnie zgadza), należy sprawdzić nazwę kontenera za pomocą 
    ```bash
    docker ps
    ```
- Przejść do katalogu *hexapod_controller* w sklonowanym repozytorium, jeżeli kontener automatycznie się w nim nie uruchomi
    ```bash
    cd ~/HEXAPOD/hexapod_controller
    ```
- Skompilować program do wersji wykonywalnej przez środowisko ROS2
    ```bash
    colcon build
    ```
- Upewnić się, że wszystkie źródła są aktualne (do pliku .bashrc zostały dodane wszystkie zależne źródła w trakcie tworzenia obrazu docker - plik *dockerfile* od linii 45)
    ```bash
    source ~/.bashrc
    ```
- Uruchomić moduł główny robota
    ```bash
    ros2 launch hexapod_controller hexapod.launch.py
    ```
- Uruchomić moduł sterowania z klawiatury w nowym terminalu (dodatkowa sesja ssh, podzielenie terminalu za pomocą VSCode), dla którego należy również połączyć się do aktywnej sesji docker
    ```bash
    docker exec -it docker_ros2_1 bash
    ```
    ```bash
    ros2 run hexapod_controller keyboard_node
    ```
 Po skończonej zabawie można zamknąć aplikację w obu terminalach (każdy osobno) za pomocą kombinacji "Ctrl + C".

---

## Wyłączanie programu

Po skończonej zabawie można zamknąć aplikację w obu terminalach (każdy osobno) za pomocą kombinacji "Ctrl + C".
Gdy to zrobimy, to możemy wyjść z kontenera,
```bash
exit
```
a następnie możemy wyłączyć aktywny obraz.
```bash
docker stop docker_ros2_1
```
Po wyłączeniu obrazu możemy bezpiecznie wyłączyć Raspberry.
```bash
sudo shutdown now
```
Po zgaśnięciu diody zielonej (chwilę miga po wyłączeniu), która sygnalizuje aktywny zapis na karcie SD, możemy odłączyć przewód zasilający.

---

## Kolejne uruchomienia programu

 Gdy raz już zbudujemy kontener i skompilujemy program, to możemy go znacznie szybciej uruchamiać:
 - Upewnić się, że konwerter TTL jest podpięty do portu USB i ma adres /dev/ttyUSB0,
    ```bash
    dmesg | grep tty
    ```
    jeżeli konwerter ma inny adres, należy zmienić go na odpowiedni w pliku *docker-compose.yml* w sekcji *devices*.
- Przejść do folderu **docker** w repozytorium
    ```bash
    cd ~/HEXAPOD/docker
    ```
- Uruchomić nasz kontener z ustawieniami zawartymi w *docker-compose.yml*
    ```bash
    docker-compose up -d
    ```
- Uruchomić interaktywną sesję dla działającego kontenera
    ```bash
    docker exec -it docker_ros2_1 bash
    ```
- Uruchomić moduł główny robota
    ```bash
    ros2 launch hexapod_controller hexapod.launch.py
    ```
- Uruchomić moduł sterowania z klawiatury w nowym terminalu (dodatkowa sesja ssh, podzielenie terminalu za pomocą VSCode), dla którego należy również połączyć się do aktywnej sesji docker
    ```bash
    docker exec -it docker_ros2_1 bash
    ```
    ```bash
    ros2 run hexapod_controller keyboard_node
    ```

---

## Troubleshooting

---

**Q:** Zmieniłem konwerter i program przestał działać - co teraz?

**A:** Gdyby wymagana była zmiana portu konwertera TTL lub wydarzyła się ona samoistnie, to po jej dokonaniu należy sprawdzić, jaki otrzymał on numer.
```bash
dmesg | grep tty
```
Po ustaleniu numeru należy go zmienić w ustawieniach (w pliku *docker-compose.yml*) i na nowo uruchomić kontener. Tutaj jednak może się okazać, że nasz program nie działa, pomimo uruchomienia kontenera. W takim przypadku należy wykorzystać plik o adekwatnej nazwie "whyDoIhaveToDoThis.txt", znajdującym się w folderze docker/ i skopiować całą jego zawartość. Skopiowaną treść należy wkleić w oknie terminala (w kontenerze) i wcisnąć przycisk "Enter".

---

**Q:** Wywołanie polecenia ```colcon build``` skutkuje pojawieniem się błędów i aplikacja nie działa.

**A:** Należy usunąć katalogi instalacyjne
```bash
rm -rf ~/HEXAPOD/hexapod_controller/build ~/HEXAPOD/hexapod_controller/install ~/HEXAPOD/hexapod_controller/log
```
i jeszcze raz wywołać polecenie
```bash
colcon build
```