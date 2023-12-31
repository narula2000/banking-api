from rest_framework.test import APITestCase
from transfer.factories import TransferFactory
from account.factories import AccountFactory


class TransferTestCase(APITestCase):
    transfer_enpoint = '/api/v1/transfer/'
    transfers_endpoint = '/api/v1/transfers/'
    def setUp(self):
        self.from_account = AccountFactory()
        self.to_account = AccountFactory()


    def test_transfer_negative_amount(self):
        # Make the transfer
        response = self.client.post(self.transfer_enpoint, {
            'from_account': self.from_account.id,
            'to_account': self.to_account.id,
            'amount': -200
        })

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['error'], 'Amount must be positive.')

    def test_transfer_zero_amount(self):
        # Make the transfer
        response = self.client.post(self.transfer_enpoint, {
            'from_account': self.from_account.id,
            'to_account': self.to_account.id,
            'amount': 0
        })

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['error'], 'Amount must be positive.')


    def test_overdraft(self):
        # Make the transfer
        response = self.client.post(self.transfer_enpoint, {
            'from_account': self.from_account.id,
            'to_account': self.to_account.id,
            'amount': 20000
        })

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['error'], 'Insufficient balance.')

    def test_transfer_with_invalid_data(self):
        # Make the transfer
        response = self.client.post(self.transfer_enpoint, {
            'from_account': self.from_account.id,
            'to_account': self.to_account.id,
            'amount': "Invalid data"
        })

        self.assertEqual(response.status_code, 400)


    def test_transfer(self):
        TransferFactory(from_account=self.from_account, to_account=self.to_account)

        # Make the transfer
        response = self.client.post(self.transfer_enpoint, {
            'from_account': self.from_account.id,
            'to_account': self.to_account.id,
            'amount': 200
        })

        self.assertEqual(response.status_code, 201)

        # Refresh the account instances to get the updated balances
        self.from_account.refresh_from_db()
        self.to_account.refresh_from_db()

        self.assertEqual(self.from_account.balance, 800)  # Assuming balance was deducted
        self.assertEqual(self.to_account.balance, 1200)  # Assuming balance was added

    def test_list_all_transfers(self):
        # Create 2 transfers
        TransferFactory(from_account=self.from_account, to_account=self.to_account)
        TransferFactory(from_account=self.from_account, to_account=self.to_account)

        response = self.client.get(self.transfers_endpoint)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_get_invalid_transfer(self):
        response = self.client.get(f'{self.transfer_enpoint}100/')

        self.assertEqual(response.status_code, 404)

    def test_get_transfer(self):
        transfer = TransferFactory(from_account=self.from_account, to_account=self.to_account)

        response = self.client.get(f'{self.transfer_enpoint}{transfer.id}/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], transfer.id)
