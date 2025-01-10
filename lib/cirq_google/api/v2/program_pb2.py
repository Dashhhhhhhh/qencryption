# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cirq_google/api/v2/program.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n cirq_google/api/v2/program.proto\x12\x12\x63irq.google.api.v2\"\xd7\x01\n\x07Program\x12.\n\x08language\x18\x01 \x01(\x0b\x32\x1c.cirq.google.api.v2.Language\x12.\n\x07\x63ircuit\x18\x02 \x01(\x0b\x32\x1b.cirq.google.api.v2.CircuitH\x00\x12\x30\n\x08schedule\x18\x03 \x01(\x0b\x32\x1c.cirq.google.api.v2.ScheduleH\x00\x12/\n\tconstants\x18\x04 \x03(\x0b\x32\x1c.cirq.google.api.v2.ConstantB\t\n\x07program\"\x93\x01\n\x08\x43onstant\x12\x16\n\x0cstring_value\x18\x01 \x01(\tH\x00\x12\x34\n\rcircuit_value\x18\x02 \x01(\x0b\x32\x1b.cirq.google.api.v2.CircuitH\x00\x12*\n\x05qubit\x18\x03 \x01(\x0b\x32\x19.cirq.google.api.v2.QubitH\x00\x42\r\n\x0b\x63onst_value\"\xd4\x01\n\x07\x43ircuit\x12K\n\x13scheduling_strategy\x18\x01 \x01(\x0e\x32..cirq.google.api.v2.Circuit.SchedulingStrategy\x12+\n\x07moments\x18\x02 \x03(\x0b\x32\x1a.cirq.google.api.v2.Moment\"O\n\x12SchedulingStrategy\x12#\n\x1fSCHEDULING_STRATEGY_UNSPECIFIED\x10\x00\x12\x14\n\x10MOMENT_BY_MOMENT\x10\x01\"}\n\x06Moment\x12\x31\n\noperations\x18\x01 \x03(\x0b\x32\x1d.cirq.google.api.v2.Operation\x12@\n\x12\x63ircuit_operations\x18\x02 \x03(\x0b\x32$.cirq.google.api.v2.CircuitOperation\"P\n\x08Schedule\x12\x44\n\x14scheduled_operations\x18\x03 \x03(\x0b\x32&.cirq.google.api.v2.ScheduledOperation\"`\n\x12ScheduledOperation\x12\x30\n\toperation\x18\x01 \x01(\x0b\x32\x1d.cirq.google.api.v2.Operation\x12\x18\n\x10start_time_picos\x18\x02 \x01(\x03\"?\n\x08Language\x12\x14\n\x08gate_set\x18\x01 \x01(\tB\x02\x18\x01\x12\x1d\n\x15\x61rg_function_language\x18\x02 \x01(\t\"k\n\x08\x46loatArg\x12\x15\n\x0b\x66loat_value\x18\x01 \x01(\x02H\x00\x12\x10\n\x06symbol\x18\x02 \x01(\tH\x00\x12/\n\x04\x66unc\x18\x03 \x01(\x0b\x32\x1f.cirq.google.api.v2.ArgFunctionH\x00\x42\x05\n\x03\x61rg\":\n\x08XPowGate\x12.\n\x08\x65xponent\x18\x01 \x01(\x0b\x32\x1c.cirq.google.api.v2.FloatArg\":\n\x08YPowGate\x12.\n\x08\x65xponent\x18\x01 \x01(\x0b\x32\x1c.cirq.google.api.v2.FloatArg\"Q\n\x08ZPowGate\x12.\n\x08\x65xponent\x18\x01 \x01(\x0b\x32\x1c.cirq.google.api.v2.FloatArg\x12\x15\n\ris_physical_z\x18\x02 \x01(\x08\"v\n\x0ePhasedXPowGate\x12\x34\n\x0ephase_exponent\x18\x01 \x01(\x0b\x32\x1c.cirq.google.api.v2.FloatArg\x12.\n\x08\x65xponent\x18\x02 \x01(\x0b\x32\x1c.cirq.google.api.v2.FloatArg\"\xad\x01\n\x0cPhasedXZGate\x12\x30\n\nx_exponent\x18\x01 \x01(\x0b\x32\x1c.cirq.google.api.v2.FloatArg\x12\x30\n\nz_exponent\x18\x02 \x01(\x0b\x32\x1c.cirq.google.api.v2.FloatArg\x12\x39\n\x13\x61xis_phase_exponent\x18\x03 \x01(\x0b\x32\x1c.cirq.google.api.v2.FloatArg\";\n\tCZPowGate\x12.\n\x08\x65xponent\x18\x01 \x01(\x0b\x32\x1c.cirq.google.api.v2.FloatArg\"\x7f\n\x08\x46SimGate\x12+\n\x05theta\x18\x01 \x01(\x0b\x32\x1c.cirq.google.api.v2.FloatArg\x12)\n\x03phi\x18\x02 \x01(\x0b\x32\x1c.cirq.google.api.v2.FloatArg\x12\x1b\n\x13translate_via_model\x18\x03 \x01(\x08\">\n\x0cISwapPowGate\x12.\n\x08\x65xponent\x18\x01 \x01(\x0b\x32\x1c.cirq.google.api.v2.FloatArg\"e\n\x0fMeasurementGate\x12$\n\x03key\x18\x01 \x01(\x0b\x32\x17.cirq.google.api.v2.Arg\x12,\n\x0binvert_mask\x18\x02 \x01(\x0b\x32\x17.cirq.google.api.v2.Arg\"@\n\x08WaitGate\x12\x34\n\x0e\x64uration_nanos\x18\x01 \x01(\x0b\x32\x1c.cirq.google.api.v2.FloatArg\"\xa7\t\n\tOperation\x12*\n\x04gate\x18\x01 \x01(\x0b\x32\x18.cirq.google.api.v2.GateB\x02\x18\x01\x12\x30\n\x08xpowgate\x18\x07 \x01(\x0b\x32\x1c.cirq.google.api.v2.XPowGateH\x00\x12\x30\n\x08ypowgate\x18\x08 \x01(\x0b\x32\x1c.cirq.google.api.v2.YPowGateH\x00\x12\x30\n\x08zpowgate\x18\t \x01(\x0b\x32\x1c.cirq.google.api.v2.ZPowGateH\x00\x12<\n\x0ephasedxpowgate\x18\n \x01(\x0b\x32\".cirq.google.api.v2.PhasedXPowGateH\x00\x12\x38\n\x0cphasedxzgate\x18\x0b \x01(\x0b\x32 .cirq.google.api.v2.PhasedXZGateH\x00\x12\x32\n\tczpowgate\x18\x0c \x01(\x0b\x32\x1d.cirq.google.api.v2.CZPowGateH\x00\x12\x30\n\x08\x66simgate\x18\r \x01(\x0b\x32\x1c.cirq.google.api.v2.FSimGateH\x00\x12\x38\n\x0ciswappowgate\x18\x0e \x01(\x0b\x32 .cirq.google.api.v2.ISwapPowGateH\x00\x12>\n\x0fmeasurementgate\x18\x0f \x01(\x0b\x32#.cirq.google.api.v2.MeasurementGateH\x00\x12\x30\n\x08waitgate\x18\x10 \x01(\x0b\x32\x1c.cirq.google.api.v2.WaitGateH\x00\x12\x38\n\x0cinternalgate\x18\x11 \x01(\x0b\x32 .cirq.google.api.v2.InternalGateH\x00\x12@\n\x10\x63ouplerpulsegate\x18\x12 \x01(\x0b\x32$.cirq.google.api.v2.CouplerPulseGateH\x00\x12\x38\n\x0cidentitygate\x18\x13 \x01(\x0b\x32 .cirq.google.api.v2.IdentityGateH\x00\x12\x30\n\x08hpowgate\x18\x14 \x01(\x0b\x32\x1c.cirq.google.api.v2.HPowGateH\x00\x12N\n\x17singlequbitcliffordgate\x18\x15 \x01(\x0b\x32+.cirq.google.api.v2.SingleQubitCliffordGateH\x00\x12\x39\n\x04\x61rgs\x18\x02 \x03(\x0b\x32\'.cirq.google.api.v2.Operation.ArgsEntryB\x02\x18\x01\x12)\n\x06qubits\x18\x03 \x03(\x0b\x32\x19.cirq.google.api.v2.Qubit\x12\x1c\n\x14qubit_constant_index\x18\x06 \x03(\x05\x12\x15\n\x0btoken_value\x18\x04 \x01(\tH\x01\x12\x1e\n\x14token_constant_index\x18\x05 \x01(\x05H\x01\x1a\x44\n\tArgsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.cirq.google.api.v2.Arg:\x02\x38\x01\x42\x0c\n\ngate_valueB\x07\n\x05token\"\x12\n\x04Gate\x12\n\n\x02id\x18\x01 \x01(\t\"\x13\n\x05Qubit\x12\n\n\x02id\x18\x02 \x01(\t\"\x9c\x01\n\x03\x41rg\x12\x31\n\targ_value\x18\x01 \x01(\x0b\x32\x1c.cirq.google.api.v2.ArgValueH\x00\x12\x10\n\x06symbol\x18\x02 \x01(\tH\x00\x12/\n\x04\x66unc\x18\x03 \x01(\x0b\x32\x1f.cirq.google.api.v2.ArgFunctionH\x00\x12\x18\n\x0e\x63onstant_index\x18\x04 \x01(\x05H\x00\x42\x05\n\x03\x61rg\"\xcf\x02\n\x08\x41rgValue\x12\x15\n\x0b\x66loat_value\x18\x01 \x01(\x02H\x00\x12:\n\x0b\x62ool_values\x18\x02 \x01(\x0b\x32#.cirq.google.api.v2.RepeatedBooleanH\x00\x12\x16\n\x0cstring_value\x18\x03 \x01(\tH\x00\x12\x16\n\x0c\x64ouble_value\x18\x04 \x01(\x01H\x00\x12\x39\n\x0cint64_values\x18\x05 \x01(\x0b\x32!.cirq.google.api.v2.RepeatedInt64H\x00\x12;\n\rdouble_values\x18\x06 \x01(\x0b\x32\".cirq.google.api.v2.RepeatedDoubleH\x00\x12;\n\rstring_values\x18\x07 \x01(\x0b\x32\".cirq.google.api.v2.RepeatedStringH\x00\x42\x0b\n\targ_value\"\x1f\n\rRepeatedInt64\x12\x0e\n\x06values\x18\x01 \x03(\x03\" \n\x0eRepeatedDouble\x12\x0e\n\x06values\x18\x01 \x03(\x01\" \n\x0eRepeatedString\x12\x0e\n\x06values\x18\x01 \x03(\t\"!\n\x0fRepeatedBoolean\x12\x0e\n\x06values\x18\x01 \x03(\x08\"B\n\x0b\x41rgFunction\x12\x0c\n\x04type\x18\x01 \x01(\t\x12%\n\x04\x61rgs\x18\x02 \x03(\x0b\x32\x17.cirq.google.api.v2.Arg\"\xaf\x02\n\x10\x43ircuitOperation\x12\x1e\n\x16\x63ircuit_constant_index\x18\x01 \x01(\x05\x12M\n\x18repetition_specification\x18\x02 \x01(\x0b\x32+.cirq.google.api.v2.RepetitionSpecification\x12\x33\n\tqubit_map\x18\x03 \x01(\x0b\x32 .cirq.google.api.v2.QubitMapping\x12\x46\n\x13measurement_key_map\x18\x04 \x01(\x0b\x32).cirq.google.api.v2.MeasurementKeyMapping\x12/\n\x07\x61rg_map\x18\x05 \x01(\x0b\x32\x1e.cirq.google.api.v2.ArgMapping\"\xbc\x01\n\x17RepetitionSpecification\x12S\n\x0erepetition_ids\x18\x01 \x01(\x0b\x32\x39.cirq.google.api.v2.RepetitionSpecification.RepetitionIdsH\x00\x12\x1a\n\x10repetition_count\x18\x02 \x01(\x05H\x00\x1a\x1c\n\rRepetitionIds\x12\x0b\n\x03ids\x18\x01 \x03(\tB\x12\n\x10repetition_value\"\xac\x01\n\x0cQubitMapping\x12<\n\x07\x65ntries\x18\x01 \x03(\x0b\x32+.cirq.google.api.v2.QubitMapping.QubitEntry\x1a^\n\nQubitEntry\x12&\n\x03key\x18\x01 \x01(\x0b\x32\x19.cirq.google.api.v2.Qubit\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.cirq.google.api.v2.Qubit\"$\n\x0eMeasurementKey\x12\x12\n\nstring_key\x18\x01 \x01(\t\"\xe2\x01\n\x15MeasurementKeyMapping\x12N\n\x07\x65ntries\x18\x01 \x03(\x0b\x32=.cirq.google.api.v2.MeasurementKeyMapping.MeasurementKeyEntry\x1ay\n\x13MeasurementKeyEntry\x12/\n\x03key\x18\x01 \x01(\x0b\x32\".cirq.google.api.v2.MeasurementKey\x12\x31\n\x05value\x18\x02 \x01(\x0b\x32\".cirq.google.api.v2.MeasurementKey\"\xa0\x01\n\nArgMapping\x12\x38\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\'.cirq.google.api.v2.ArgMapping.ArgEntry\x1aX\n\x08\x41rgEntry\x12$\n\x03key\x18\x01 \x01(\x0b\x32\x17.cirq.google.api.v2.Arg\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.cirq.google.api.v2.Arg\"\xcd\x01\n\x0cInternalGate\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06module\x18\x02 \x01(\t\x12\x12\n\nnum_qubits\x18\x03 \x01(\x05\x12\x41\n\tgate_args\x18\x04 \x03(\x0b\x32..cirq.google.api.v2.InternalGate.GateArgsEntry\x1aH\n\rGateArgsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.cirq.google.api.v2.Arg:\x02\x38\x01\"\xd8\x03\n\x10\x43ouplerPulseGate\x12\x37\n\x0chold_time_ps\x18\x01 \x01(\x0b\x32\x1c.cirq.google.api.v2.FloatArgH\x00\x88\x01\x01\x12\x37\n\x0crise_time_ps\x18\x02 \x01(\x0b\x32\x1c.cirq.google.api.v2.FloatArgH\x01\x88\x01\x01\x12:\n\x0fpadding_time_ps\x18\x03 \x01(\x0b\x32\x1c.cirq.google.api.v2.FloatArgH\x02\x88\x01\x01\x12\x37\n\x0c\x63oupling_mhz\x18\x04 \x01(\x0b\x32\x1c.cirq.google.api.v2.FloatArgH\x03\x88\x01\x01\x12\x38\n\rq0_detune_mhz\x18\x05 \x01(\x0b\x32\x1c.cirq.google.api.v2.FloatArgH\x04\x88\x01\x01\x12\x38\n\rq1_detune_mhz\x18\x06 \x01(\x0b\x32\x1c.cirq.google.api.v2.FloatArgH\x05\x88\x01\x01\x42\x0f\n\r_hold_time_psB\x0f\n\r_rise_time_psB\x12\n\x10_padding_time_psB\x0f\n\r_coupling_mhzB\x10\n\x0e_q0_detune_mhzB\x10\n\x0e_q1_detune_mhz\"\x8b\x01\n\x0f\x43liffordTableau\x12\x17\n\nnum_qubits\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x1a\n\rinitial_state\x18\x02 \x01(\x05H\x01\x88\x01\x01\x12\n\n\x02rs\x18\x03 \x03(\x08\x12\n\n\x02xs\x18\x04 \x03(\x08\x12\n\n\x02zs\x18\x05 \x03(\x08\x42\r\n\x0b_num_qubitsB\x10\n\x0e_initial_state\"O\n\x17SingleQubitCliffordGate\x12\x34\n\x07tableau\x18\x01 \x01(\x0b\x32#.cirq.google.api.v2.CliffordTableau\"!\n\x0cIdentityGate\x12\x11\n\tqid_shape\x18\x01 \x03(\r\":\n\x08HPowGate\x12.\n\x08\x65xponent\x18\x01 \x01(\x0b\x32\x1c.cirq.google.api.v2.FloatArgB/\n\x1d\x63om.google.cirq.google.api.v2B\x0cProgramProtoP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cirq_google.api.v2.program_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\035com.google.cirq.google.api.v2B\014ProgramProtoP\001'
  _LANGUAGE.fields_by_name['gate_set']._options = None
  _LANGUAGE.fields_by_name['gate_set']._serialized_options = b'\030\001'
  _OPERATION_ARGSENTRY._options = None
  _OPERATION_ARGSENTRY._serialized_options = b'8\001'
  _OPERATION.fields_by_name['gate']._options = None
  _OPERATION.fields_by_name['gate']._serialized_options = b'\030\001'
  _OPERATION.fields_by_name['args']._options = None
  _OPERATION.fields_by_name['args']._serialized_options = b'\030\001'
  _INTERNALGATE_GATEARGSENTRY._options = None
  _INTERNALGATE_GATEARGSENTRY._serialized_options = b'8\001'
  _globals['_PROGRAM']._serialized_start=57
  _globals['_PROGRAM']._serialized_end=272
  _globals['_CONSTANT']._serialized_start=275
  _globals['_CONSTANT']._serialized_end=422
  _globals['_CIRCUIT']._serialized_start=425
  _globals['_CIRCUIT']._serialized_end=637
  _globals['_CIRCUIT_SCHEDULINGSTRATEGY']._serialized_start=558
  _globals['_CIRCUIT_SCHEDULINGSTRATEGY']._serialized_end=637
  _globals['_MOMENT']._serialized_start=639
  _globals['_MOMENT']._serialized_end=764
  _globals['_SCHEDULE']._serialized_start=766
  _globals['_SCHEDULE']._serialized_end=846
  _globals['_SCHEDULEDOPERATION']._serialized_start=848
  _globals['_SCHEDULEDOPERATION']._serialized_end=944
  _globals['_LANGUAGE']._serialized_start=946
  _globals['_LANGUAGE']._serialized_end=1009
  _globals['_FLOATARG']._serialized_start=1011
  _globals['_FLOATARG']._serialized_end=1118
  _globals['_XPOWGATE']._serialized_start=1120
  _globals['_XPOWGATE']._serialized_end=1178
  _globals['_YPOWGATE']._serialized_start=1180
  _globals['_YPOWGATE']._serialized_end=1238
  _globals['_ZPOWGATE']._serialized_start=1240
  _globals['_ZPOWGATE']._serialized_end=1321
  _globals['_PHASEDXPOWGATE']._serialized_start=1323
  _globals['_PHASEDXPOWGATE']._serialized_end=1441
  _globals['_PHASEDXZGATE']._serialized_start=1444
  _globals['_PHASEDXZGATE']._serialized_end=1617
  _globals['_CZPOWGATE']._serialized_start=1619
  _globals['_CZPOWGATE']._serialized_end=1678
  _globals['_FSIMGATE']._serialized_start=1680
  _globals['_FSIMGATE']._serialized_end=1807
  _globals['_ISWAPPOWGATE']._serialized_start=1809
  _globals['_ISWAPPOWGATE']._serialized_end=1871
  _globals['_MEASUREMENTGATE']._serialized_start=1873
  _globals['_MEASUREMENTGATE']._serialized_end=1974
  _globals['_WAITGATE']._serialized_start=1976
  _globals['_WAITGATE']._serialized_end=2040
  _globals['_OPERATION']._serialized_start=2043
  _globals['_OPERATION']._serialized_end=3234
  _globals['_OPERATION_ARGSENTRY']._serialized_start=3143
  _globals['_OPERATION_ARGSENTRY']._serialized_end=3211
  _globals['_GATE']._serialized_start=3236
  _globals['_GATE']._serialized_end=3254
  _globals['_QUBIT']._serialized_start=3256
  _globals['_QUBIT']._serialized_end=3275
  _globals['_ARG']._serialized_start=3278
  _globals['_ARG']._serialized_end=3434
  _globals['_ARGVALUE']._serialized_start=3437
  _globals['_ARGVALUE']._serialized_end=3772
  _globals['_REPEATEDINT64']._serialized_start=3774
  _globals['_REPEATEDINT64']._serialized_end=3805
  _globals['_REPEATEDDOUBLE']._serialized_start=3807
  _globals['_REPEATEDDOUBLE']._serialized_end=3839
  _globals['_REPEATEDSTRING']._serialized_start=3841
  _globals['_REPEATEDSTRING']._serialized_end=3873
  _globals['_REPEATEDBOOLEAN']._serialized_start=3875
  _globals['_REPEATEDBOOLEAN']._serialized_end=3908
  _globals['_ARGFUNCTION']._serialized_start=3910
  _globals['_ARGFUNCTION']._serialized_end=3976
  _globals['_CIRCUITOPERATION']._serialized_start=3979
  _globals['_CIRCUITOPERATION']._serialized_end=4282
  _globals['_REPETITIONSPECIFICATION']._serialized_start=4285
  _globals['_REPETITIONSPECIFICATION']._serialized_end=4473
  _globals['_REPETITIONSPECIFICATION_REPETITIONIDS']._serialized_start=4425
  _globals['_REPETITIONSPECIFICATION_REPETITIONIDS']._serialized_end=4453
  _globals['_QUBITMAPPING']._serialized_start=4476
  _globals['_QUBITMAPPING']._serialized_end=4648
  _globals['_QUBITMAPPING_QUBITENTRY']._serialized_start=4554
  _globals['_QUBITMAPPING_QUBITENTRY']._serialized_end=4648
  _globals['_MEASUREMENTKEY']._serialized_start=4650
  _globals['_MEASUREMENTKEY']._serialized_end=4686
  _globals['_MEASUREMENTKEYMAPPING']._serialized_start=4689
  _globals['_MEASUREMENTKEYMAPPING']._serialized_end=4915
  _globals['_MEASUREMENTKEYMAPPING_MEASUREMENTKEYENTRY']._serialized_start=4794
  _globals['_MEASUREMENTKEYMAPPING_MEASUREMENTKEYENTRY']._serialized_end=4915
  _globals['_ARGMAPPING']._serialized_start=4918
  _globals['_ARGMAPPING']._serialized_end=5078
  _globals['_ARGMAPPING_ARGENTRY']._serialized_start=4990
  _globals['_ARGMAPPING_ARGENTRY']._serialized_end=5078
  _globals['_INTERNALGATE']._serialized_start=5081
  _globals['_INTERNALGATE']._serialized_end=5286
  _globals['_INTERNALGATE_GATEARGSENTRY']._serialized_start=5214
  _globals['_INTERNALGATE_GATEARGSENTRY']._serialized_end=5286
  _globals['_COUPLERPULSEGATE']._serialized_start=5289
  _globals['_COUPLERPULSEGATE']._serialized_end=5761
  _globals['_CLIFFORDTABLEAU']._serialized_start=5764
  _globals['_CLIFFORDTABLEAU']._serialized_end=5903
  _globals['_SINGLEQUBITCLIFFORDGATE']._serialized_start=5905
  _globals['_SINGLEQUBITCLIFFORDGATE']._serialized_end=5984
  _globals['_IDENTITYGATE']._serialized_start=5986
  _globals['_IDENTITYGATE']._serialized_end=6019
  _globals['_HPOWGATE']._serialized_start=6021
  _globals['_HPOWGATE']._serialized_end=6079
# @@protoc_insertion_point(module_scope)