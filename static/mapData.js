/*

Esse mapa é baseado em vetores.
Aqui está o código que cria o mapa na tela com as funções de zoom
também é possível alterar o texto que aparece quando o mouse passa
em uma "feature" no mapa.

*/

const resX = 800;
const resY = 400;

const buildingData = {
    type: 'FeatureCollection',
    features: [
        {
            type: 'Feature',
            geometry: {
                type: 'MultiLineString',
                coordinates: [[
                    [1106 - resX, -68 + resY],
                    // [1106 - resX, -321 + resY],
                    // [954 - resX, -321 + resY],
                    // [954 - resX, -68 + resY],
                ]],
            },
        },
    ],
};

// salas (o que chamo de "feature" em "mapSrc.js")
const roomsData = {
    // todas ficam no seguinte formato:
    type: 'FeatureCollection',              // array de features/salas
    features: [
        {
            type: 'Feature',                // sempre "feature" para aparecer os quadrados que representam as salas
            properties: {                           
                name: 'Exemplo feature',    // nome da sala
                devNum: 5,                  // quantidade de aparelhos na respectiva sala (aqui deverá ser incluída a integração)
            },
            geometry: {
                type: 'Polygon',            // polígono de quatro lados
                coordinates: [[             // coordenadas dos lados 
                                            // o "resX" e "resY" representam a resolução da coordenada para caberem no mapa
                    [954 - resX, -68 + resY],
                    [954 - resX, -321 + resY],
                    [1106 - resX, -321 + resY],
                    [1106 - resX, -68 + resY],
                ]],                         
            },
        },
    ],
};