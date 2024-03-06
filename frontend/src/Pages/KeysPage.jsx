import React from 'react';
import SearchKeys from '../Components/SearchKeys';
import KeysCard from '../Components/KeysCard';
import axios from "axios";

const baseURL = "https://jsonplaceholder.typicode.com/users";

const data = [
    {
        "id" : 1,
        "name": "Vasya",
        "room": 200,
    },
    {
        "id" : 1,
        "name": "Masha",
        "room": 205,
    },
    {
        "id" : 1,
        "name": "Petya",
        "room": 400,
    }
];

const renderCards = data.map((card)=>
    <KeysCard  person={card.name} room={card.room}/>
)
 function KeysPage(){
    const [user, setUser] = React.useState(null);

    React.useEffect(() => {
        axios.get(baseURL).then((response) => {
          setUser(response.data);
        });
      }, []);


    if (!user) return null;
    return (
        <div>
            <div className="request-header p-4 ps-5">
                <h1>Выданные ключи</h1>
            </div>
        <SearchKeys/>
          <div className="container d-flex justify-content-center flex-column w-75">
          {/* <KeysCard  person={user.name}/>
          <KeysCard  person="Иванова Ивана Ивановича"/> */}
        {renderCards}
          </div>

        </div>
    );
}
export default KeysPage;