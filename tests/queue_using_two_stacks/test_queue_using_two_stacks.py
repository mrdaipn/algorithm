import pytest
from problems.queue_with_two_stacks.queue_with_two_stacks import CubeWithTwoStacks

@pytest.fixture()
def queue():
    return CubeWithTwoStacks()


def test_enqueu_dequeue_should_work(queue):    
    queue.enqueue(12)
    queue.enqueue(10)
    
    v1 = queue.dequeue()
    assert v1 == 12

    queue.enqueue(15)
    
    v2 = queue.dequeue()
    assert v2 == 10

    v3 = queue.dequeue()
    assert v3 == 15


def test_dequeu_empty_queue_should_return_none(queue):    
    assert None  == queue.dequeue()


def test_peek_queue_should_return_the_first_item_without_removing_it(queue):
    queue.enqueue(10)
    queue.enqueue(12)

    p = queue.peek()
    assert p == 10
    assert queue.length == 2

def test_peek_empty_queue_should_return_none(queue):
    p = queue.peek()
    assert p is None


