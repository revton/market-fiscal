# Tesseract

## Instalar
```zsh
brew install tesseract --all-languages
```

## Configurar 

- Verificar valor da variável de ambiente TESSDATA_PREFIX
```zsh
echo $TESSDATA_PREFIX
```

- Definir variável de ambiente
```sh
echo 'export TESSDATA_PREFIX="/Users/revton/homebrew/share/tessdata/"' >> ~/.zshenv
source ~/.zshenv
```

- Verificar valor da variável de ambiente TESSDATA_PREFIX
```zsh
echo $TESSDATA_PREFIX
```







