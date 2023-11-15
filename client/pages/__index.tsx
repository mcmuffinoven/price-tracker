import React, {useEffect, useState} from 'react';
import Chart from './chart';
import DashboardExample from './dashboard';
import ItemStatus from './card_table';
import '@fontsource/roboto/300.css';
import '@fontsource/roboto/400.css';
import '@fontsource/roboto/500.css';
import '@fontsource/roboto/700.css';

function index() {
  const [message, setMessage] = useState("Loading");
  const [people, setPeople] = useState([]);

  // useEffect(() => {
  //   fetch("http://localhost:8080/api/home")
  //     .then((response) => response.json())
  //     .then((data) => {
  //       // Loading message on load
  //       setMessage(data.message);
  //       setPeople(data.people);
  //     })
  // }, []);

  return (
    <div>
      {/* <div>
        {message}
      </div>
      {people.map((person,index) =>(
        <div key={index}>
          {person}
        </div>
      ))} */}
      <DashboardExample></DashboardExample>
      <div className="mt-6 gap-6">
        <ItemStatus></ItemStatus>
      </div>
    </div>
  );
}

export default index;