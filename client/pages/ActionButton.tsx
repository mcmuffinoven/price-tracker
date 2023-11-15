import React from 'react'
import { Button } from '@mui/material';
import { createTheme } from '@mui/material/styles';
import { green, purple, blue, red } from '@mui/material/colors';

const useStyles:any = makeStyles(theme => ({
    root: {
        minWidth: 0,
        margin: theme.spacing(0.5)
    },
    secondary: {
        backgroundColor: theme.palette.secondary.light,
        '& .MuiButton-label': {
            color: theme.palette.secondary.main,
        }
    },
    primary: {
        backgroundColor: theme.palette.primary.light,
        '& .MuiButton-label': {
            color: theme.palette.primary.main,
        }
    },
}))


const theme = createTheme({
  palette: {
    primary: {
      main: blue[500],
    },
    secondary: {
      main: red[500],
    },
  },
});


export default function ActionButton(props:any) {

    const { color, children, onClick } = props;
    const classes = useStyles();

    return (
        <Button
            sx={{

            }}
            onClick={onClick}>
            {children}
        </Button>
    )
}