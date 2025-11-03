OK_FORMAT = True

test = {   'name': 'q2',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> def test_vae_loss():\n'
                                               '...     input1 = torch.tensor([[0., 1., 1., 0., 0.],\n'
                                               '...             [0., 1., 0., 0., 0.],\n'
                                               '...             [0., 0., 1., 1., 1.]])\n'
                                               '...     input2 = torch.tensor([[0.6238, 0.7332, 0.4550, 0.8462, 0.3369],\n'
                                               '...             [0.0094, 0.8038, 0.2322, 0.6135, 0.3734],\n'
                                               '...             [0.4059, 0.7136, 0.1875, 0.5227, 0.3589]])\n'
                                               '...     assert torch.isclose(reconst_loss(input1, input2), torch.tensor(709.3800))\n'
                                               '...     input3 = torch.tensor([[0.3164, 0.9965, 0.5840, 0.2150, 0.7718],\n'
                                               '...             [0.2923, 0.3308, 0.0867, 0.3817, 0.3926],\n'
                                               '...             [0.6635, 0.5653, 0.6097, 0.0394, 0.8974]])\n'
                                               '...     input4 = torch.tensor([[0.1780, 0.2826, 0.8356, 0.1315, 0.5268],\n'
                                               '...             [0.0396, 0.4332, 0.4000, 0.3398, 0.2645],\n'
                                               '...             [0.4005, 0.2803, 0.0625, 0.4183, 0.9721]])\n'
                                               '...     assert torch.isclose(kl_div(input3, input4), torch.tensor(2.9696))\n'
                                               '>>> test_vae_loss()\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
