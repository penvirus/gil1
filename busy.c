#include <Python.h>
#include <time.h>
#include <stdio.h>
#include <stdint.h>

void busy_wait(unsigned int duration)
{
	uint64_t count = 0;
	time_t begin = time(NULL);

	while(1) {
		if(time(NULL) - begin > duration)
			break;
		count++;
	}

	printf("busy_wait(): count = %" PRIu64 "\n", count);
}

static PyObject *with_lock(PyObject *self, PyObject *args)
{
	unsigned int duration;

	if(!PyArg_ParseTuple(args, "I", &duration))
		return NULL;

	busy_wait(duration);

	Py_INCREF(Py_None);
	return Py_None;
}

static PyObject *without_lock(PyObject *self, PyObject *args)
{
	unsigned int duration;

	if(!PyArg_ParseTuple(args, "I", &duration))
		return NULL;

	PyThreadState *_save;
	_save = PyEval_SaveThread();
	busy_wait(duration);
	PyEval_RestoreThread(_save);

	Py_INCREF(Py_None);
	return Py_None;
}

static PyMethodDef busy_methods[] = {
	{"with_lock", with_lock, METH_VARARGS, "Busy wait for a given duration with GIL"},
	{"without_lock", without_lock, METH_VARARGS, "Busy wait for a given duration without GIL"},
	{NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC initbusy(void)
{
	if(Py_InitModule("busy", busy_methods) == NULL)
		return PyErr_SetString(PyExc_RuntimeError, "failed to Py_InitModule");
}
