"""
Write a program to find the intersecting point of two lined lists.
"""

def findMergeNode(head1, head2):
    p1=head1
    p2=head2
    while 1:
        if p1==p2:
            break
        p1=p1.next
        p2=p2.next
        if p1 is None:
            p1=head2
        if p2 is None:
            p2=head1
    return p1.data