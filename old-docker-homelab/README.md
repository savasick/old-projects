# <strong> Docker - Homelab </strong>

dont touch it

Collection of the applications used in homelabs, with self-signed certificates\
All in one compose.file


| Application | Description |
| :--------  | ---------: |
| [traefik](https://traefik.io) | Edge Router |
| [adminer](https://www.adminer.org) | database management |
| [gitea](https://about.gitea.com) | git server |
| [portainer](https://www.portainer.io) | container orchestration |
| [heimdall](https://github.com/linuxserver/Heimdall) | home page |

#


<details>
<summary><strong>INSTALLATION</strong></summary>

</br>


1. <strong>Get mkcert</strong>

    <big><strong>linux</strong></big>
    
    install network security service libraries
    ```bash
    sudo apt install libnss3-tools -y
    ```

    get <a href="https://brew.sh/">brew</a>.
    when get it, install mkcert

    ```bash
    brew install mkcert
    ```

    #

    <big><strong>macos</strong></big>

    get <a href="https://brew.sh/">brew</a>.
    when get it, install mkcert / nss
    
    ```bash
    brew install mkcert
    brew install nss
    ```

    #

    <big><strong>windows</strong></big>

    get <a href="https://chocolatey.org/install">chocolatey</a>.
    when get it, install mkcert

    ```shell
    choco install mkcert
    ```

#

2. <strong>Get self-signed certificates</strong>
    
    creates a local certification authority and registers it in the system’s trusted storage

    ```bash
    mkcert -install
    ```


    add certificates for apps

    ```bash
    mkcert -cert-file certs/certificate.pem -key-file certs/privatekey.pem "traefik.localhost" "gitea.localhost" "adminer.localhost" "portainer.localhost" "home.localhost" "drone.localhost"

    mkcert -cert-file apps-files/postgres/server.crt -key-file apps-files/postgres/server.key "postgres"
    ```
    
#

3. <strong>Now ready to start</strong>

    ```bash
    docker-compose up -d --build
    ```
    then visit\
    https://home.localhost


</details>


#

<h3>endpoints:</h3>

[traefik.localhost](https://traefik.localhost)\
[adminer.localhost](https://adminer.localhost)\
[gitea.localhost](https://gitea.localhost)\
[portainer.localhost](https://portainer.localhost)\
[home.localhost](https://home.localhost)

#

<details>
<summary><strong>COMMANDS</strong></summary>


```bash
# delete certificates
rm -rf certs/certificate.pem certs/privatekey.pem apps-files/postgres/server.crt apps-files/postgres/server.key
```


```bash
# delete data
rm -rf data || sudo rm -rf data
```

</details>
