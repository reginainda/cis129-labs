{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "51032e9d-dd9c-4d0a-8859-3b1e31271d37",
   "metadata": {},
   "outputs": [],
   "source": [
    "# my coffee and muffin shop"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6f4acb42-7f07-4b80-99f5-5bf8d4a515ce",
   "metadata": {},
   "outputs": [],
   "source": [
    "# calculate cost of muffins plus cost of coffee. include tax"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2b230a85-b68b-486e-9eec-2f95bd2f03d7",
   "metadata": {},
   "outputs": [],
   "source": [
    "# ask the user how many coffees they are going to purchase"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a9c1d8b4-fb60-4225-ba0a-ec716acd1960",
   "metadata": {},
   "outputs": [],
   "source": [
    "# ask the user how many muffins they are going to purchase"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ba88f1fc-0404-4fb9-bcd0-8367bcce18c4",
   "metadata": {},
   "outputs": [],
   "source": [
    "num_coffees = int(input(\"How many coffees is the customer purchasing? \"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6c65c791-c0bc-4979-b557-eb0be818697b",
   "metadata": {},
   "outputs": [],
   "source": [
    "num_muffins = int(input(\"How many muffins is the customer purchasing? \"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1dce557d-347c-4594-bffe-66cc6ffe38a4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# prices for coffee and muffins"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e9ed9407-3ba5-4da6-81a1-aaaf57e4552a",
   "metadata": {},
   "outputs": [],
   "source": [
    "price_for_coffee = 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "845d6358-b17a-46f8-be26-eeb4feebba8c",
   "metadata": {},
   "outputs": [],
   "source": [
    "price_for_muffins = 4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "16a423d7-3eb3-46de-8c05-d2353de8feca",
   "metadata": {},
   "outputs": [],
   "source": [
    "# calculate price of coffee and muffins before tax"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d95a295a-693b-422a-9f7e-9a8e1f0d7658",
   "metadata": {},
   "outputs": [],
   "source": [
    "subtotal = (num_coffees * price_for_muffins) + (num_muffins * price_for_muffins)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "91bb81d2-39af-4b10-89d6-a5b8e6b03813",
   "metadata": {},
   "outputs": [],
   "source": [
    "# calculate tax. don't add subtotal yet"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b68f4fba-e916-444e-a931-1874b1060d21",
   "metadata": {},
   "outputs": [],
   "source": [
    "tax = subtotal * 0.06"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5bddb702-27fc-4b85-899b-607fe3cbde64",
   "metadata": {},
   "outputs": [],
   "source": [
    "# add subtotal and tax"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5d54f651-a601-4b87-98f5-c4224cdaa4ac",
   "metadata": {},
   "outputs": [],
   "source": [
    "total = tax + subtotal "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5c3a7275-1591-4153-a9ab-68cf08267dc1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# receipt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "25d9b96d-72f4-40bd-a5cf-bfa1b62d3497",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(\"\\nMy Coffee and Muffin Shop Reciept\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7d849459-a1b1-4131-af28-4ca9823160a7",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(str(num_coffees) + Coffee at $5 per coffee: $\" + str(round(num_coffees * price_for_coffee, 2)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d3dafb35-bb6a-470c-b22a-70ff3d1f7ff8",
   "metadata": {},
   "outputs": [],
   "source": [
    "#this will round the price"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "58c3c0d5-96da-4fe9-9467-33c3083a310c",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(str(num_muffins) + \" Muffins at $4 each: $\" + str(round(num_muffins * price_for_muffins, 2)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3d67e318-4563-4048-ac55-cfd5e6e4f8a4",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(\"tax 6%: $\" str(round(tax, 2)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7d501f3b-955c-4dec-9b2a-8b541d1d0007",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(\"Total: $\" + str(round(total, 2)))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "anaconda-ai-2024.04-py310",
   "language": "python",
   "name": "conda-env-anaconda-ai-2024.04-py310-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
