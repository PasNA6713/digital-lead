// export default{
//   actions: {
//     // Настроить получение с backend
//     catchPlacemarks(context){
//       let messages
//         axios
//           .get('https://293dc3a83292.ngrok.io/message/get/')
//           .then(response => (messages = response));
//       context.commit("updatePlacemarksOnMap", messages);
//     }
    
//   },



//   mutations: {
//     updatePlacemarksOnMap(state, messages){
//       // проверить на уникальность новых placemarks?

//       // Распределение по цветам
//       for (let i=0;i<messages.length;i++){
//         state.placemarks["features"].push({
//             type: 'Feature',
//             id: messages[i]["id"],
//             geometry: {
//                 type: 'Point',
//                 coordinates: [messages[i]["longtitude"], messages[i]["latitude"]]
//             },
//             properties: {
//                 hintContent: messages[i]["datetime"],
//                 balloonContent: messages[i]["text"]
//             },
//             options: {
//                 preset: "islands#dotIcon",
//                 iconColor: state.classifier[messages[i]["danger_level"]]
//             }
//         })
//         }
//     }
//   },



//   state: {
//       placemarks: {
//         "type": "FeatureCollection",
//         "features": [
//           {
//             type: 'Feature',
//             id: 3,
//             geometry: {
//                 type: 'Point',
//                 coordinates: [59.9, 30.55]
//             },
//             properties: {
//                 hintContent: 'Содержание всплывающей подсказки',
//                 balloonContent: 'Содержание балуна'
//             },
//             options: {
//                 preset: "islands#dotIcon",
//                 iconColor: "blue"
//             }
//         }   
//         ],
//       },
//       myMap: null,
//       objectManager: null,
//       messages: null,
//       classifier: {
//           1: 'yellow',
//           2: 'blue',
//           3: 'red'
//       },      
//   },


//   getters: {
//       getAllPlacemarks(state){
//         return state.placemarks["features"];
//     },
//       getAllPlacemarksCount(state){
//         return state.placemarks["features"].length;
//     }
//   }
// }
