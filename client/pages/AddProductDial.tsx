import React, {useState} from 'react';
import Box from '@mui/material/Box';
import SpeedDial from '@mui/material/SpeedDial';
import SpeedDialIcon from '@mui/material/SpeedDialIcon';
import SpeedDialAction from '@mui/material/SpeedDialAction';
import ShareIcon from '@mui/icons-material/Share';
import QueueIcon from '@mui/icons-material/Queue';

import Popup from './Popup';
import ProductForm from './NewProductForm';

const actions = [
  { icon: <QueueIcon />, name: 'Add Product', operation: "add product"},
  { icon: <ShareIcon />, name: 'Delete Product', operation: "delete product" },
];


export default function BasicSpeedDial(props:any) {
    const [openPopup, setOpenPopup] = useState(false)
  return (
    <Box sx={{ height: 0, transform: 'translateZ(0px)', flexGrow: 1 }}>
      <SpeedDial
        ariaLabel="SpeedDial basic example"
        sx={{position: 'absolute', bottom: 16, right: 16 }}
        icon={<SpeedDialIcon />}
        direction='down'
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