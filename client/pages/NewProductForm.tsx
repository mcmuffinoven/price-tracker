import React, {useState} from 'react';
import Stack from '@mui/material/Stack';
import TextField from '@mui/material/TextField';
import { Button } from '@mui/material';
import MenuItem from '@mui/material/MenuItem';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import { red } from '@mui/material/colors';

const categories = [
  {
    value: 'Tech',
    label: 'Tech',
  },
  {
    value: 'Grocery',
    label: 'Grocery',
  },
  {
    value: 'Fashion',
    label: 'Fashion',
  },
  {
    value: 'Cosmetics',
    label: 'Cosmetics',
  },
];

export default function ProductForm(props:any) {

    const {openPopup, setOpenPopup, user} = props;
    const [productName, setProductName] = useState('')
    const [productLink, setProductLink] = useState('')
    const [productDate, setProductDate] = useState('')
    const [productCategory, setProductCategory] = useState('')
    
    const handleSubmit=(event:any) =>{
      event.preventDefault();
      console.log('Product:',productName, 'Link:', productLink, 'Date:', productDate, 'Category:', productCategory); 
      const postData = JSON.stringify({
        "productName": productName,
        "productLink": productLink,
        "trackedSinceDate": productDate,
        "category": productCategory,
        "user": user.sid
      })
      console.log(postData)
      fetch('http://localhost:8080/api/addProduct', {
        method: 'POST',
        body: postData,
        headers: {
          'Content-type': 'application/json; charset=UTF-8',
        },
      })
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            window.location.reload();
            // Handle data
        })
        .catch((err) => {
            console.log(err.message);
        });
  }

  return (
    <>
      <form onSubmit={handleSubmit}>
        <Stack 
              direction="column"
              justifyContent="space-evenly"
              alignItems="flex-start"
              spacing={3}>

            <TextField
                type="text"
                variant='outlined'
                color='secondary'
                label="Product Name"
                helperText="Name of product"
                onChange={e => setProductName(e.target.value)}
                value={productName}
                fullWidth
                required
                sx={{mb: 4}}
            />
          <TextField
              type="url"
              variant='outlined'
              color='secondary'
              label="Product Link"
              helperText="Link to product"
              onChange={e => setProductLink(e.target.value)}
              value={productLink}
              fullWidth
              required
              sx={{mb: 4}}
          />
          <TextField
              type="date"
              variant='outlined'
              color='secondary'
              helperText="Optional: Set deadline date"
              onChange={e => setProductDate(e.target.value)}
              value={productDate}
              sx={{mb: 4}}
          ><DatePicker></DatePicker></TextField>
          <TextField
            id="outlined-select-currency"
            select
            label="Select"
            helperText="Select a category"
            onChange={e => setProductCategory(e.target.value)}
            value={productCategory}
            sx={{mb: 4}}
          >
            {categories.map((option) => (
              <MenuItem key={option.value} value={option.value}>
                {option.label}
              </MenuItem>
            ))} 
          </TextField>
          <Stack 
              direction="row"
              justifyContent="flex-end"
              alignItems="stretch"
              spacing={3}>
            <Button variant="outlined" color="primary" type="submit" sx={{mb: 4}} onClick={()=>{setOpenPopup(false)}}>Add</Button>
            <Button variant="outlined" sx={{borderColor: red[500], color:red[500], mb: 4}} onClick={()=>{setOpenPopup(false)}}>Cancel</Button>
          </Stack>
        </Stack>
    </form>
    </>
  );
}