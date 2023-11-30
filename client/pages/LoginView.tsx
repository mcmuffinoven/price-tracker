import React, {JSXElementConstructor, useEffect, useState} from 'react';

import {Container, Box, Grid, Paper, Stack, Typography} from "@mui/material"
import PrimarySearchAppBar from './AppBar';
import DataTable from './Table';
import BasicSpeedDial from './AddProductDial';

function LoginView(props:any) {
  const {user} = props
  return (
    <div className = "App">
      <PrimarySearchAppBar></PrimarySearchAppBar>
      <Container>

        <Stack sx={{marginY:5}}>
          <Box>
            <DataTable user={user}></DataTable>
          </Box>
          <Box>
            <BasicSpeedDial user={user}></BasicSpeedDial>
          </Box>
        </Stack>        
      </Container>
    </div>
  )
}

export default LoginView