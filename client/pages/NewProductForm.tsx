import React, {useState} from 'react';
import { IMaskInput } from 'react-imask';
import { NumericFormat, NumericFormatProps } from 'react-number-format';
import Stack from '@mui/material/Stack';
import Input from '@mui/material/Input';
import InputLabel from '@mui/material/InputLabel';
import TextField from '@mui/material/TextField';
import FormControl from '@mui/material/FormControl';
import { Button } from '@mui/material';
import MenuItem from '@mui/material/MenuItem';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import { red } from '@mui/material/colors';

interface CustomProps {
  onChange: (event: { target: { name: string; value: string } }) => void;
  name: string;
}

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

const TextMaskCustom = React.forwardRef<HTMLInputElement, CustomProps>(
  function TextMaskCustom(props, ref) {
    const { onChange, ...other } = props;
    return (
      <IMaskInput
        {...other}
        mask="(#00) 000-0000"
        definitions={{
          '#': /[1-9]/,
        }}
        inputRef={ref}
        onAccept={(value: any) => onChange({ target: { name: props.name, value } })}
        overwrite
      />
    );
  },
);

const NumericFormatCustom = React.forwardRef<NumericFormatProps, CustomProps>(
  function NumericFormatCustom(props, ref) {
    const { onChange, ...other } = props;

    return (
      <NumericFormat
        {...other}
        getInputRef={ref}
        onValueChange={(values) => {
          onChange({
            target: {
              name: props.name,
              value: values.value,
            },
          });
        }}
        thousandSeparator
        valueIsNumericString
        prefix="$"
      />
    );
  },
);

export default function FormattedInputs() {
  const [values, setValues] = React.useState({
    textmask: '(100) 000-0000',
    numberformat: '1320',
  });

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setValues({
      ...values,
      [event.target.name]: event.target.value,
    });
  };

    const [firstName, setFirstName] = useState('')
    const [lastName, setLastName] = useState('')
    const [email, setEmail] = useState('')
    const [dateOfBirth, setDateOfBirth] = useState('')
    
    function handleSubmit(event:any) {
        event.preventDefault();
        console.log(firstName, lastName, email, dateOfBirth) 
    }
    
  return (
    <>
      <form>
        {/* <Stack direction="row" spacing={2}>
          <FormControl variant="standard">
            <InputLabel htmlFor="formatted-text-mask-input">react-imask</InputLabel>
            <Input
              value={values.textmask}
              onChange={handleChange}
              name="textmask"
              id="formatted-text-mask-input"
              inputComponent={TextMaskCustom as any}
            />
          </FormControl>

          <TextField
            label="react-number-format"
            value={values.numberformat}
            onChange={handleChange}
            name="numberformat"
            id="formatted-numberformat-input"
            InputProps={{
              inputComponent: NumericFormatCustom as any,
            }}
            variant="standard"
          />
        </Stack> */}
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
                onChange={e => setFirstName(e.target.value)}
                value={firstName}
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
              onChange={e => setEmail(e.target.value)}
              value={email}
              fullWidth
              required
              sx={{mb: 4}}
          />
          <TextField
              type="date"
              variant='outlined'
              color='secondary'
              helperText="Optional: Set deadline date"
              onChange={e => setDateOfBirth(e.target.value)}
              value={dateOfBirth}
              sx={{mb: 4}}
          ><DatePicker></DatePicker></TextField>
          <TextField
            id="outlined-select-currency"
            select
            label="Select"
            helperText="Select a category"
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
            <Button variant="outlined" color="primary" type="submit" sx={{mb: 4}}>Add</Button>
            <Button variant="outlined" sx={{borderColor: red[500], color:red[500], mb: 4}} type="submit">Cancel</Button>
          </Stack>
        </Stack>
    </form>
    </>
  );
}