



$('#vector-map').dxVectorMap({
    maxZoomFactor: 5,   // fator de máximo zoom do mapa
    // cada zoom divide/multiplica as coordenadas por 500
    projection: {
      to(coordinates) {
        return [coordinates[0] / 500, coordinates[1] / 500];
      },

      from(coordinates) {
        return [coordinates[0] * 500, coordinates[1] * 500];
      },
    },
    // cria as linhas que cercam o mapa
    layers: [{
      hoverEnabled: false,
      dataSource: buildingData, // chama as coordenadas do esqueleto definidas em "mapData.js"
      name: 'building',
    },
    // cria as "features" que podem ser alteradas depois
    {
      color: 'orange',          // cor das features
      opacity: '40%',           // opacidade
      onclick() { alert("") },
      borderWidth: 1,           // tamanho da bordas das features
      label: {        
        enabled: true,        
        dataField: 'name',      // nome que aparece em cima do retângulo da feature
      },
      dataSource: roomsData,    // chama as cooredenadas das features definidas em "mapData.js"
      name: 'rooms',            // procura as "rooms" definidas em "mapData.js"
    }],
    // quando passa o cursor em uma feature
    tooltip: {
      enabled: true,
      customizeTooltip(arg) {
        if (arg.layer.name === 'rooms') {
          // retorna um balão com a seguinte mensagem
          return { text: `Aparelhos na área: ${arg.attribute('devNum')} aparelho` };
        }
        return null;
      },
    },
  });
