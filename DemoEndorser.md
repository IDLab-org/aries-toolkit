# Helm Chart pour mettre en place une PoC d'accréditation

### Lancement rapide

1. [Optionnel] Construire et publier une image pour ACAPY (valider la version acapy et modifier le tag par votre registre)
    ```
    docker build -t <IMAGE_REGISTRY>/acapy:0.8.1 -f Dockerfile.acapy ./docker
    docker push <IMAGE_REGISTRY>/acapy:0.8.1

    ```

2. [Optionnel] Générer les secrets
    ```
    cd helm/acapy
    python3 -m venv venv
    . venv/bin/activate
    pip install base58, jinja2, PyNaCl
    ./generate_secrets.py

    ```

3. Enregistrer les DID dans le registre visé (Candy-dev par défaut) avec le role `endorser` pour l'accéditeur et `none` pour l'auteur
    * Prendre en note les `seed` pour des déploiements future

4. Installer le Chart dans la namespace désirée
    ```
    helm upgrade endorser-demo . \
    --namespace <NAMESPACE> \
    --values ./secret_values.yaml \
    --create-namespace --install

    ```

5. Valider le déploiement. Prendre en note les erreures rencontrées et les solutions. Bonifier la documentation de mises en garde si nécessaire.
