import React, {useEffect, useState} from 'react';

import {Container, Grid, Typography} from "@mui/material"
import { TourCard, Prod, Category} from './TourCard';
import PrimarySearchAppBar from './AppBar';
import cats from "./products.json"
import DataGridDemo from './Table';
import SparklineColumn from './SparkTable';
import BasicSpeedDial from './AddProductDial';
import Stack from '@mui/material/Stack';

function index() {

  // const [message, setMessage] = useState("Loading");
  // const [products, setProducts] = useState([] as Prod[]);
  // const [categories, setCategories] = useState([] as Category[])
  // useEffect(() => {
  //   fetch("http://localhost:8080/api/home")
  //     .then((response) => response.json())
  //     .then((data) => {
  //       // Loading message on load
  //       setCategories(data)
  //     })
  // }, []);
  // console.log(products)
  return (
    <div className = "App">
      <PrimarySearchAppBar></PrimarySearchAppBar>
        {/* <Container sx={{marginY:5}}>
          {cats.map((category)=>(
            <>
              <Typography 
                variant="h4"
                component="h2"
                marginTop={5}
                marginBottom={3}>{category.category}</Typography>

              <Grid container spacing={5}>
                    {category.productList.map((item, index)=><TourCard obj={item} key={item.id}/>)}
              </Grid>
            </>
          ))}

        </Container> */}
        {/* <Container sx={{marginY:5}}>
          <SingleLineGridList></SingleLineGridList>
        </Container> */}

          <Container sx={{marginY:5}}>
            <DataGridDemo></DataGridDemo>
            {/* <SparklineColumn></SparklineColumn> */}
          <BasicSpeedDial></BasicSpeedDial>
          </Container>
    </div>
  )
}

export default index