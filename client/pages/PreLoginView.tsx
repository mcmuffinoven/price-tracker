import * as React from 'react';
import Stack from '@mui/material/Stack';
import Paper from '@mui/material/Paper';
import { styled } from '@mui/material/styles';
import { Box } from '@mui/material';
import Typography from '@mui/material/Typography';
import { Button } from '@mui/material';

const DemoPaper = styled(Paper)(({ theme }) => ({
  padding: theme.spacing(4),
  ...theme.typography.body2,
  textAlign: 'center',
}));

export default function PreLoginView() {
  return (
    <Box
  display="flex"
  justifyContent="center"
  alignItems="center"
  minHeight="100vh"
>
    <DemoPaper elevation={16}>

    <Stack >
        <Typography variant="h3" gutterBottom> Product Price Tracking</Typography>
        <Typography variant="subtitle1" gutterBottom>
          Helps keep track of products of interests and alerts when it is on sale.
        </Typography>
        <Button href="/api/auth/login" variant="contained">Login To Continue</Button>
    </Stack>
    </DemoPaper>
</Box>
        
      


            // <Box sx={{ display: 'inline-flex'}}>
            //     <DemoPaper>

            //     <Typography variant="h1" gutterBottom> h1. Heading </Typography>
            //     <Button href="/api/auth/login" variant="contained">Login</Button>
            //     </DemoPaper>
            // </Box>
  );
}