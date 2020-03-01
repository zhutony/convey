# RUST_BACKTRACE=1;RUST_LOG=debug ./target/debug/convey --config sample-proxy.toml 
./target/debug/convey --config sample-proxy.toml 

# DEBUG 2020-03-01T05:30:32Z: convey::proxy: *** exiting from listing on the front port.
# DEBUG 2020-03-01T05:30:32Z: convey::proxy::backend: Running backend health checkerBackend { name: "tcp3000_out", servers: RwLock { s: Semaphore { state: SemState { permits: 32 }, head: 0x7f83b7b00598, rx_lock: 0, stub: Waiter 
# { state: 0, waker: AtomicWaker, next: 0x0 } }, c: UnsafeCell }, health_check_interval: 3 }, Interval { delay: Delay { registration: Registration { entry: Entry { time: CachePadded(UnsafeCell), inner: (Weak), state: 18001, wake
# r: AtomicWaker, queued: false, next_atomic: UnsafeCell, when: UnsafeCell, next_stack: UnsafeCell, prev_stack: UnsafeCell } } }, period: 3s }
# thread 'tokio-runtime-worker' panicked at 'failed to open /dev/urandom: Os { code: 24, kind: Other, message: "Too many open files" }', src/libstd/sys/unix/rand.rs:90:24
# note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

# DEBUG 2020-03-01T06:02:33Z: convey::proxy: accept: V4(192.168.55.1:58634)
# DEBUG 2020-03-01T06:02:34Z: convey::proxy: ERR: Os { code: 24, kind: Other, message: "Too many open files" }
# DEBUG 2020-03-01T06:02:34Z: convey::proxy: *** exiting from listing on the front port.

# curl http://localhost:7000/stats

