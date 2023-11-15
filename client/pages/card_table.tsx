import { useState } from "react";
import {
    Card,
    Title,
    Text,
    Flex,
    Table,
    TableRow,
    TableCell,
    TableHead,
    TableHeaderCell,
    TableBody,
    Badge,
    Button,
    Select,
    SelectItem,
  } from "@tremor/react";
  
  const colors = {
    "Ready for dispatch": "gray",
    Cancelled: "rose",
    Shipped: "emerald",
  };
  

  export type Product = {
    transactionID: string,
    user: string,
    item: string,
    status: string,
    category: string,
    amount: string,
    link: string,
  };

  const transactions: Product[]  = [
    {
      transactionID: "#123456",
      user: "Lena Mayer",
      item: "Under Armour Shorts",
      status: "Ready for dispatch",
      category: "Tech",
      amount: "$ 49.90",
      link: "#",
    },
    {
      transactionID: "#234567",
      user: "Max Smith",
      item: "Book - Wealth of Nations",
      status: "Ready for dispatch",
      category: "Tech",
      amount: "$ 19.90",
      link: "#",
    },
    {
      transactionID: "#345678",
      user: "Anna Stone",
      item: "Garmin Forerunner 945",
      status: "Cancelled",
      category: "Tech",
      amount: "$ 499.90",
      link: "#",
    },
    {
      transactionID: "#4567890",
      user: "Truls Cumbersome",
      item: "Running Backpack",
      status: "Shipped",
      category: "Tech",
      amount: "$ 89.90",
      link: "#",
    },
    {
      transactionID: "#5678901",
      user: "Peter Pikser",
      item: "Rolex Submariner Replica",
      status: "Cancelled",
      category: "Tech",
      amount: "$ 299.90",
      link: "#",
    },
    {
      transactionID: "#6789012",
      user: "Phlipp Forest",
      item: "On Clouds Shoes",
      status: "Ready for dispatch",
      category: "Tech",
      amount: "$ 290.90",
      link: "#",
    },
    {
      transactionID: "#78901234",
      user: "Mara Pacemaker",
      item: "Ortovox Backpack 40l",
      status: "Shipped",
      category: "Food",
      amount: "$ 150.00",
      link: "#",
    },
    {
      transactionID: "#89012345",
      user: "Sev Major",
      item: "Oakley Jawbreaker",
      status: "Ready for dispatch",
      category: "Fashion",
      amount: "$ 190.90",
      link: "#",
    },
  ];
  
  export default function Example() {
    const [selectedCategory, setSelectedCategory] = useState("all");


    const isCategorySelected = (product: Product) =>
        (product.category === selectedCategory || selectedCategory === "all");

    return (
      <Card>
        <Flex justifyContent="start" className="space-x-2">
          <Title>Purchases</Title>
          <Badge color="gray">8</Badge>
        </Flex>
        <Text className="mt-2">Overview of this month's purchases</Text>
        <Select
            className="max-w-full sm:max-w-xs"
            defaultValue="all"
            onValueChange={setSelectedCategory}
        >
            <SelectItem value="all">All Categories</SelectItem>
            <SelectItem value="Tech">Tech</SelectItem>
            <SelectItem value="Fashion">Fashion</SelectItem>
            <SelectItem value="Food">Food</SelectItem>
        </Select>
        <Table className="mt-6">
          <TableHead>
            <TableRow>
              <TableHeaderCell>Transaction ID</TableHeaderCell>
              <TableHeaderCell>User</TableHeaderCell>
              <TableHeaderCell>Item</TableHeaderCell>
              <TableHeaderCell>Status</TableHeaderCell>
              <TableHeaderCell>Category</TableHeaderCell>
              <TableHeaderCell className="text-right">Amount</TableHeaderCell>
              <TableHeaderCell>Link</TableHeaderCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {transactions.filter((item) => isCategorySelected(item)).map((item) => (
              <TableRow key={item.transactionID}>
                <TableCell>{item.transactionID}</TableCell>
                <TableCell>{item.user}</TableCell>
                <TableCell>{item.item}</TableCell>
                <TableCell>
                  <Badge color={colors[item.status]} size="xs">
                    {item.status}
                  </Badge>
                </TableCell>
                <TableCell>{item.category}</TableCell>
                <TableCell className="text-right">{item.amount}</TableCell>
                <TableCell>
                  <Button size="xs" variant="secondary" color="gray">
                    See details
                  </Button>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </Card>
    );
  }