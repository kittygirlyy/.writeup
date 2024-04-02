import hashlib
 import angr
import claripy
 
LOGIN = "root-me.org"
FILE_LEN = 0x20
 
def main():
    print("Loading")
    proj = angr.Project("ch36.bin", auto_load_libs=False)
 
    key = [claripy.BVS(f"key_{i}", 8) for i in range(FILE_LEN)]
    fdin = claripy.Concat(*key)
 
    state = proj.factory.call_state(0x00400146, "root-me.org\n", fdin)
 
    print("Starting !")
    sm = proj.factory.simulation_manager(state)
    sm.explore(find=0x00400182, avoid=0x0040017b)
 
    cracked_key: bytes = sm.found[0].solver.eval(fdin, cast_to=bytes)[:len(LOGIN)]
    print(f"Found sha256: {hashlib.sha256(cracked_key).hexdigest()}")
 
 
if __name__ == "__main__":
    main()