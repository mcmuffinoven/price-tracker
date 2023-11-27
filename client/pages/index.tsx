import React, {useEffect, useState} from 'react';

import {Container, Box, Grid, Paper, Stack, Typography} from "@mui/material"
import PrimarySearchAppBar from './AppBar';
import DataTable from './Table';
import BasicSpeedDial from './AddProductDial';

function index() {
  return (
    <div className = "App">
      <PrimarySearchAppBar></PrimarySearchAppBar>
      <Container>

        <Stack sx={{marginY:5}}>
          <Box>
            <DataTable></DataTable>
          </Box>
          <Box>
            <BasicSpeedDial></BasicSpeedDial>
          </Box>
        </Stack>        
      </Container>
    </div>
  )
}

export default index