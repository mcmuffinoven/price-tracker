import React from "react";
import {Dialog, DialogTitle, DialogContent} from '@mui/material'
import Typography from '@mui/material/Typography';
import CloseRoundedIcon from '@mui/icons-material/CloseRounded';
import {Container} from "@mui/material"
import { Button} from "@mui/material";
import { red } from '@mui/material/colors';
import Stack from "@mui/material/Stack";



export default function Popup(props:any){
    
    const {title, children, openPopup, setOpenPopup} = props;

    return (
        <Dialog open={openPopup} maxWidth="md">
            <DialogTitle>
                <Stack direction="row" spacing={2}>

                    <Typography variant="h6">
                        {title}
                    </Typography>
                    <Button 
                        sx={{marginLeft:10,
                            backgroundColor: red[500],
                            '&:hover': {
                            backgroundColor: red[700],
                          },
                        }}
                        variant="contained" onClick={()=>{setOpenPopup(false)}}>
                        <CloseRoundedIcon/>
                    </Button>
                </Stack>
            </DialogTitle>
            <DialogContent dividers>
                {children}
            </DialogContent>
        </Dialog>
    )
}