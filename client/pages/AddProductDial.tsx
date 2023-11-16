import React, {useState} from 'react';
import Box from '@mui/material/Box';
import SpeedDial from '@mui/material/SpeedDial';
import SpeedDialIcon from '@mui/material/SpeedDialIcon';
import SpeedDialAction from '@mui/material/SpeedDialAction';
import FileCopyIcon from '@mui/icons-material/FileCopyOutlined';
import SaveIcon from '@mui/icons-material/Save';
import PrintIcon from '@mui/icons-material/Print';
import ShareIcon from '@mui/icons-material/Share';

import Popup from './Popup';
import ProductForm from './NewProductForm';

const actions = [
  { icon: <FileCopyIcon />, name: 'Copy', operation: "copy"},
  { icon: <SaveIcon />, name: 'Save' },
  { icon: <PrintIcon />, name: 'Print' },
  { icon: <ShareIcon />, name: 'Share' },
];


export default function BasicSpeedDial() {
    // function handleClick (e:any,operation:any){
    //     e.preventDefault();
    //     if(operation=="copy"){
    //       // do something 
    //         console.log("Copy")
    //         return <MaxWidthDialog></MaxWidthDialog>
    //     }else if(operation=="tag"){
    //       //do something else
    //     }
    //     // setOpen(!open);// to close the speed dial, remove this line if not needed.
    //   };

    const [openPopup, setOpenPopup] = useState(false)
  return (
    <Box sx={{ height: 320, transform: 'translateZ(0px)', flexGrow: 1 }}>
      <SpeedDial
        ariaLabel="SpeedDial basic example"
        sx={{ position: 'absolute', bottom: 16, right: 16 }}
        icon={<SpeedDialIcon />}
        // FabProps={{ size: "medium", style: { backgroundColor: "#2196f3" } }}
      >
        {actions.map((action) => (
          <SpeedDialAction
            key={action.name}
            icon={action.icon}
            tooltipTitle={action.name}
            onClick={()=> setOpenPopup(true)}
          />
        ))}
      </SpeedDial>
      <Popup 
        title = "Track new product"
        openPopup = {openPopup}
        setOpenPopup = {setOpenPopup}>
          <ProductForm 
            openPopup = {openPopup}
            setOpenPopup = {setOpenPopup}></ProductForm>
      </Popup>
    </Box>
  );
}