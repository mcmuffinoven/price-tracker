import React, {useEffect, useState} from 'react';

import {Container, Grid, Typography} from "@mui/material"
import { TourCard, Prod, Category} from './TourCard';
import PrimarySearchAppBar from './AppBar';
import cats from "./products.json"
import DataTable from './Table';
import BasicSpeedDial from './AddProductDial';

function index() {
  return (
    <div className = "App">
      <PrimarySearchAppBar></PrimarySearchAppBar>        
          <Container sx={{marginY:5}}>
            <DataTable></DataTable>
            {/* <SparklineColumn></SparklineColumn> */}
          <BasicSpeedDial></BasicSpeedDial>
          </Container>
    </div>
  )
}

export default index