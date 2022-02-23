# Copyright (c) 2020  PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .base import BaseHead
from .tsn_head import TSNHead
from .tsm_head import TSMHead
from .pptsm_head import ppTSMHead
from .pptsn_head import ppTSNHead
from .slowfast_head import SlowFastHead
from .attention_lstm_head import AttentionLstmHead
from .timesformer_head import TimeSformerHead
from .stgcn_head import STGCNHead
from .msg3d_head import MSG3DHead
from .dgcn_head import DGCNHead
from .i3d_head import I3DHead

__all__ = [
    'BaseHead', 'TSNHead', 'TSMHead', 'ppTSMHead', 'ppTSNHead', 'SlowFastHead',
    'AttentionLstmHead', 'TimeSformerHead', 'STGCNHead','MSG3DHead','DGCNHead','I3DHead'
]